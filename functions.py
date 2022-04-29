import pyperclip
import time
import pyautogui
from sys import platform

width, height = pyautogui.size()
pyautogui.PAUSE = 1


def final_click(copy: str):
    pyperclip.copy(copy)

    time.sleep(10)

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


def tmp_list(new_waves: list):
    tmp_list = []
    for index in range(len(new_waves)):
        if index % 2 == 0:
            for ind in range(len(new_waves[index - 1])):
                if ind % 2 == 1:
                    tmp_list.append(new_waves[index - 1][ind - 1])
    return tmp_list