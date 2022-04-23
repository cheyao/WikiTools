from PIL import Image
from os.path import exists
import webbrowser
from sys import platform
import re
from tkinter import Tk
import pyperclip


def main():
    final_file_name = 'output.txt'
    dir_name = int(input("""Type in level type: 1. ADVENTURE  2. ARCADE  3. CHALLENGES 4. CHECKPOINTS  5. COMMUNITY
6. ENDLESS  7. HARDCORE  8.MINIGAMES  9. SECRET  10. SURVIVAL  11. TICKDOWN  12. TRAINING  13. WARP: """))
    dir_name = getName(dir_name)

    print("You selected: " + dir_name)

    file_name = input("Type in file name: ")

    if not exists("ALPHA/" + dir_name + "/" + file_name + ".json"):
        print("~/ALPHA/" + dir_name + "/" + file_name + ".json does not exist")
        quit()

    print(f"Transforming {file_name}/{dir_name}")

    file_data = open("ALPHA/" + dir_name + "/" + file_name + ".json", "r").read()
    tmp = re.search('\"Name\": \"(\\d+-\\d+).+\",\n', file_data)
    if tmp:
        level_name = tmp.group(1)

    # openUrl(f'https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')
    print(f'opened https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')

    final_string = """{{BAHTabber|Level=1-2}}
    {{Level Infobox
    |Name=""" + re.search('\"Name\": \"(\\d+-\\d+.+)\",\n', file_data).group(1)

    pyperclip.copy(final_string)


def openUrl(fin_url: str):
    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome %s'
    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    elif platform == "win32":
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(fin_url)


def getName(input_int: int):
    if input_int == 1:
        return "ADVENTURE"
    elif input_int == 2:
        return "ARCADE"
    elif input_int == 3:
        return "CHALLENGES"
    elif input_int == 4:
        return "CHECKPOINTS"
    elif input_int == 5:
        return "COMMUNITY"
    elif input_int == 6:
        return "ENDLESS"
    elif input_int == 7:
        return "HARDCORE"
    elif input_int == 8:
        return "MINIGAMES"
    elif input_int == 9:
        return "SECRET"
    elif input_int == 10:
        return "SURVIVAL"
    elif input_int == 11:
        return "TICKDOWN"
    elif input_int == 12:
        return "TRAINING"
    elif input_int == 13:
        return "WARP"
    else:
        print("Invalid input")
        quit()


if __name__ == '__main__':
    main()
