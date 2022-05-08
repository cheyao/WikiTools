import re
import webbrowser
from tkinter.messagebox import showwarning, showerror
import pyperclip
import time
import pyautogui
from sys import platform
from tkinter import *
from tkinter import ttk
import WikiTools as wt
from tkinter import filedialog as fd
import linecache

width, height = pyautogui.size()
pyautogui.PAUSE = 1


def final_click(copy: str):
    pyperclip.copy(copy)

    time.sleep(7)

    pyautogui.moveTo(width / 2, height / 2, 1)
    pyautogui.click()
    if platform == "darwin":
        pyautogui.hotkey('command', 'v')
    elif platform == "win32":
        pyautogui.hotkey('ctrl', 'v')


def sort_zombies(zombies: list):
    sorted_list = []
    for index in range(len(zombies)):
        if index % 2 == 0:
            ordered_list = [(x, int(y)) for x, y, in zip(zombies[index - 1][::2], zombies[index - 1][1::2])]
            sorted_list.append(sum([[x, str(y)] for x, y, in sorted(ordered_list, key=lambda x:x[1])], []))
        else:
            sorted_list.append(zombies[index - 1])

    sorted_list.append(sorted_list[0])
    sorted_list.pop(0)

    return sorted_list


def openUrl(fin_url: str):
    chrome_path = "null"
    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome %s'
    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    elif platform == "win32":
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(fin_url)


def tmp_list(new_waves: list):
    tmp_list_val = []
    for index in range(len(new_waves)):
        if index % 2 == 0:
            for ind in range(len(new_waves[index - 1])):
                if ind % 2 == 1:
                    tmp_list_val.append(new_waves[index - 1][ind - 1])
    return tmp_list_val


# noinspection PyTypeChecker
def show_window():
    file_type = [('json files', '*.json')]

    def start_convert():
        if str(root.file) != 'PY_VAR0':
            convert_button.configure(text='Converting...')
            status = wt.convert(root.file)
            if status:
                convert_button.configure(text='Converted!')
            else:
                convert_button.configure(text='Error!')
        else:
            showwarning(title='Error', message='Please select a file')

    root = Tk()
    root.file = StringVar(None, 'Select')
    root.title("WikiTools")
    root.geometry("300x150")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    def select_file():
        root.file = str(fd.askopenfilename(filetypes=file_type))
        button.configure(text=re.sub('[\s\S]+/', '', str(root.file)))

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe2 = ttk.Frame(root, padding="3 3 12 12")
    mainframe2.grid(column=2, row=2, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    button = ttk.Button(mainframe, text=re.sub('[\s\S]+/', '', str(root.file.get())), command=select_file)
    button.grid(column=2, row=1, sticky=(W, E))
    convert_button = ttk.Button(mainframe, text="Convert", command=start_convert)
    convert_button.grid(column=2, row=2, sticky=W)

    ttk.Label(mainframe, text="File path:").grid(column=1, row=1, sticky=W)

    ttk.Button(mainframe2, text="Settings", command=setting).grid(column=1, row=1, sticky=W)

    root.mainloop()


# noinspection PyTypeChecker
def setting():
    file = open('template.txt', 'r').readlines()
    template = ''.join(open('template.txt', 'r').readlines()[7:])
    link_saved = ''.join(open('template.txt', 'r').readlines()[1:2])
    template_values = re.sub(r'# ', '', ''.join(open('template.txt', 'r').readlines()[3:6]))

    root = Tk()
    root.title("Setup")
    root.geometry("550x550")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe2 = ttk.Frame(root, padding="3 3 12 12")
    mainframe2.grid(column=0, row=2, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Wiki edit link, use \"{name_number}\" for level name").grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe, text="Example: \"https://project-eclise.fandom.com/wiki/{name_number}_(Alpha)?action=edit\"")\
        .grid(column=1, row=2, sticky=W)

    link_val = StringVar(root, value=link_saved)
    link = ttk.Entry(mainframe, textvariable=link_val)
    link.grid(column=1, row=3, sticky=(W, E))

    label_text = "Usable " + template_values
    ttk.Label(mainframe, text="\nWiki template.").grid(column=1, row=4, sticky=W)
    ttk.Label(mainframe, text='Use two curly brackets for one, use value inside curly brackets to add the value.')\
        .grid(column=1, row=5, sticky=W)
    ttk.Label(mainframe, text=label_text).grid(column=1, row=6, sticky=W)

    text = Text(mainframe)
    text.grid(column=1, row=7, sticky=(W, E))
    text.insert('1.0', template)

    def save_setup(link1):
        with open('template.txt', 'w') as f:
            file[1] = link1
            ''.join(file)
            file[7:] = text.get('1.0', END)
            f.writelines(file)
        root.destroy()

    ttk.Button(mainframe2, text="Save", command=lambda: save_setup(link.get())).grid(column=1, row=1, sticky=W)

    root.mainloop()


def convert(string: str) -> str:
    zombies_convert = open('convert.txt', 'r')

    for line in range(len([line.strip("\n") for line in zombies_convert if line != "\n"])):
        zombie = re.sub('\n', '', linecache.getline('convert.txt', line + 1)).split(': ')
        string = re.sub(str(zombie[0]), str(zombie[1]), string)

    return string


def error(error_message: str, level: str):
    showerror("Error", error_message + '\n' + level + "\n\n Please send this to cyao1234#2688")


if __name__ == '__main__':
    show_window()
