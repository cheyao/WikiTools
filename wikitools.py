from os.path import exists
import webbrowser
from sys import platform
import re
import pyperclip
from convert import convert


def main():
    file_path = input("Type in file path (current dir is where you placed the py file, don't write \".json\"): ")

    if not exists(file_path + ".json"):
        print("~/" + file_path + ".json does not exist")
        quit()

    print(f"Transforming ~/{file_path}.json")

    file_data = open(file_path + ".json", "r").read()
    tmp = re.search('\"Name\": \"(\\d+-\\d+).+\",\n', file_data)
    tmp2 = re.search('\"Name\": \"(\\d+-\\d+.+)\",\n', file_data)
    tmp3 = re.search('\"aliases\": \\[ \"GI\" ],\\n			\"objclass\": \"InitialGridItemProperties\",\\n			\"objdata\": {([.\\n\\t\\s\\S]+?)} ]', file_data)
    tmp4 = re.search('\"FlagCount\": (\\d+?),', file_data)
    tmp5 = re.search('\"Waves\": \\[ (.+?) ]\\n', file_data)
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
    if tmp4:
        flag_count = tmp4.group(1)
    if tmp5:
        wave_format = tmp5.group(1)
    before_level = level_name.split("-")
    before_level[0] = str(int(before_level[0]) - 1)
    before_level = "-".join(before_level)
    after_level = level_name.split("-")
    after_level[0] = str(int(after_level[0]) + 1)
    after_level = "-".join(after_level)

    wave_format = re.sub('RTID|@CurrentLevel|\\)|\\(|Wave|]|\\[|\"| |\\n', "", wave_format).split(',')

    level_place = re.search("(\\d)-", level_name).group(1)

    sorted_list = []
    for index in range(len(new_waves)):
        if index % 2 == 0:
            sorted_list.append(sorted([new_waves[index - 1][i:i+2] for i in range(0, len(new_waves[index - 1]), 2)], key=lambda x: x[1]))
        else:
            sorted_list.append(new_waves[index - 1])

    sorted_list.append(sorted_list[0])
    sorted_list.pop(0)

    print(sorted_list)
    print(wave_format)

    print(len(wave_format))
    print(len(sorted_list))
    final_list = []
    for i in range(len(wave_format)):
        #if i != 0:
        for o in range(len(sorted_list)):
            if o % 2 == 1:
                if int(wave_format[i - 1]) == int(sorted_list[o - 1]):
                    final_list.append(sorted_list[o])

    final_list.append(final_list[0])
    final_list.pop(0)
    print(final_list[0])
    print(final_list[0][::1][::2])

    final_string = ""

    for item in range(len(final_list)):
        if re.search('\"WavesPerFlag\": (\\d+),\\n', file_data).group(1) == item:
            tmp = "Flag"
        else:
            tmp = "-"

        if item == len(final_list):
            tmp2 = ""
        else:
            tmp2 = "-"
        final_string += f'|{item + 1}\n|'
        for i in range(len(final_list[item])):
            final_string += f'{final_list[item][i]}'
        final_string += '|None\n'
        final_string += f'|{tmp}\n'
        final_string += f'|{tmp2}\n'

    print(final_string)
    # openUrl(f'https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')
    print(f'opened https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')

    gravestone_count = gi.count("gravestone_egypt" or "gravestone_dark" or "gravestoneSunOnDestruction")
    no_numb_lvl_name = re.sub("\\d+?-\\d+", "", full_level_name)

    final_string = """{{{{BAHTabber|Level={}}}}}
{{{{Level Infobox
|name = {}
|image = {}Alpha.jpg
|Type = Regular
|EM = {}
|Flag = {}
|Plant = Choise
|FR =
|NR =
|before = {} (Alpha)
|after = {} (Alpha)
}}}}
\'\'\'{}\'\'\', also known as\'\'\'{}\'\'\'

{{{{clear}}}}
== Waves ==
{{| class="article-table"
!Waves
!Non-dynamic zombies
!Ambush zombies
!Notes
|-
{}""".format(level_name, full_level_name, level_name, gravestone_count, flag_count, before_level, after_level, no_numb_lvl_name, level_name, final_string)

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
