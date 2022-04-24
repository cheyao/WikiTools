from os.path import exists
import webbrowser
from sys import platform
import re
import pyperclip
from convert import convert


def main():
    dir_name = int(input("""Type in level type: 1. ADVENTURE  2. ARCADE  3. CHALLENGES 4. CHECKPOINTS  5. COMMUNITY  6. ENDLESS  7. HARDCORE  8.MINIGAMES  9. SECRET  10. SURVIVAL  11. TICKDOWN  12. TRAINING  13. WARP: """))
    dir_name = getName(dir_name)
    print(f"You selected: {dir_name}")

    file_name = input("Type in file name: ").upper()

    if not exists("ALPHA/" + dir_name + "/" + file_name + ".json"):
        print("~/ALPHA/" + dir_name + "/" + file_name + ".json does not exist")
        quit()

    print(f"Transforming ~/{dir_name}/{file_name}.json")

    file_data = open("ALPHA/" + dir_name + "/" + file_name + ".json", "r").read()
    tmp = re.search('\"Name\": \"(\\d+-\\d+).+\",\n', file_data)
    tmp2 = re.search('\"Name\": \"(\\d+-\\d+.+)\",\n', file_data)
    tmp3 = re.search('\"aliases\": \[ \"GI\" ],\\n			\"objclass\": \"InitialGridItemProperties\",\\n			\"objdata\": {([.\\n\\t\\s\\S]+?)} ]', file_data)
    waves = re.sub("\\[|]", "|", re.sub("([^\\d])]", "\\1", re.sub(
        ",|:|Type:RTID|objclass|objdata|@ZombieTypes|Zombies|}|{|\\[{Row|aliases|Row", "",
        re.sub(".+\\[]}},{aliases:|]}}],version:1}", "",
               re.sub("\\t|\\n| |\"|SpawnZombiesJitteredWaveActionProps", "", file_data))))).split("|")
    waves.remove("")

    new_waves = []
    for index in range(len(waves)):
        index += 1
        if index % 2 == 0:
            new_waves.append(re.sub("(<sup>\\d</sup>);(\\d+);({{P\\|.+?\\|2}})", "\\3 \\1#\\2#", re.sub("(<sup>\\d</sup>);<sup>0</sup>", "\\1", convert(re.sub("(\\d)\\(", "<sup>\\1</sup>(", str(waves[index - 1])))))[:-1].split("#"))
        else:
            new_waves.append(re.sub("Wave", "", str(waves[index - 1])))

    if tmp:
        level_name = tmp.group(1)
    if tmp2:
        full_level_name = tmp2.group(1)
    if tmp3:
        gi = tmp3.group(1)
    level_place = re.search("(\\d)-", level_name).group(1)

    sorted_list = []
    for index in range(len(new_waves)):
        if index % 2 == 0:
            sorted_list.append(sorted([new_waves[index - 1][i:i+2] for i in range(0, len(new_waves[index - 1]), 2)], key=lambda x: x[1]))
        else:
            sorted_list.append(new_waves[index - 1])

    sorted_list.append(sorted_list[0])
    sorted_list.pop(0)

    # openUrl(f'https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')
    print(f'opened https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')

    final_string = """{{BAHTabber|Level=1-2}}
    {{Level Infobox
    |Name = {}
    |Image = {}ALPHA.jpg
    |Type """.format(level_name, file_name)

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
