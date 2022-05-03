import re
import webbrowser
from tkinter.messagebox import showinfo
import pyperclip
import time
import pyautogui
from sys import platform
from tkinter import *
from tkinter import ttk
import WikiToolsA as a
import WikiToolsB as b
from tkinter import filedialog as fd

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
            sorted_list.append(sorted([zombies[index - 1][i:i + 2] for i in range(0, len(zombies[index - 1]), 2)],
                                      key=lambda x: x[1]))
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
    tmp_list = []
    for index in range(len(new_waves)):
        if index % 2 == 0:
            for ind in range(len(new_waves[index - 1])):
                if ind % 2 == 1:
                    tmp_list.append(new_waves[index - 1][ind - 1])
    return tmp_list


def show_window():
    file_type = [('json files', '*.json')]

    def convert():
        value = selected.get()
        if str(root.file) != 'PY_VAR0':
            convert_button.configure(text='Converting...')
            if value == 'Alpha':
                a.main(str(root.file))
            elif value == 'Beta':
                b.main(str(root.file))
        else:
            showinfo(title='Warning', message='Please select a file')

    root = Tk()
    root.file = StringVar(None, 'Select')
    root.title("WikiTools")
    root.geometry("250x165")
    # root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    def select_file():
        root.file = str(fd.askopenfilename(filetypes=file_type))
        button.configure(text=re.sub('[\s\S]+/', '', str(root.file)))

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    button = ttk.Button(mainframe, text=re.sub('[\s\S]+/', '', str(root.file.get())), command=select_file)
    button.grid(column=2, row=1, sticky=(W, E))
    convert_button = ttk.Button(mainframe, text="Convert", command=convert)
    convert_button.grid(column=2, row=2, sticky=W)

    ttk.Label(mainframe, text="File path:").grid(column=1, row=1, sticky=W)

    selected = StringVar(None, 'Alpha')
    r1 = ttk.Radiobutton(mainframe, text='Alpha', value='Alpha', variable=selected)
    r1.grid(column=3, row=1, sticky=W)
    r2 = ttk.Radiobutton(mainframe, text='Beta', value='Beta', variable=selected)
    r2.grid(column=3, row=2, sticky=W)

    root.mainloop()
