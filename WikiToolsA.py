import re
from convert import convert
import functions as f


def main(file_path: str):
    print(f"Transforming ~/{file_path}")

    file_data = open(file_path, "r").read()
    level_name_tmp = re.search('\"Name\": \"(\\d+-\\d+).+\",\n', file_data)
    full_level_name_tmp = re.search('\"Name\": \"(\\d+-\\d+.+)\",\n', file_data)
    gi_tmp = re.search(
        '\"aliases\": \\[ \"GI\" ],\\n			\"objclass\": \"InitialGridItemProperties\",\\n			\"objdata\": {([.\\n\\t\\s\\S]+?)} ]',
        file_data)
    flag_count_tmp = re.search('\"FlagCount\": (\\d+?),', file_data)
    wave_format_tmp = re.search('\"Waves\": \\[ (.+?) ]\\n', file_data)
    waves_tmp = re.sub(', {\\n\\t+\\"aliases\\": \\[ \"RM\" ][\\s\\S]+} ', ' ', re.sub('\"DinoWaveDuration\": \"\\d\"', '', file_data))
    waves_tmp2 = re.search('({\\n\\s+\"aliases\": \\[ \"Wave1\" ],\n[\\s|\\S]+\"*\\n\\t+} ]),*\n', waves_tmp).group(1)
    waves = re.sub("\\[|]", "|", re.sub("([^\\d])]", "\\1", re.sub(
        ",|:|Type:RTID|objclass|objdata|@ZombieTypes|Zombies|}|{|\\[{Row|aliases|Row|DinoWaveActionProps|DinoType:RTID|DinoRow|DinoWaveDuration|Dino|Type",
        "",
        re.sub(".+\\[]}},{aliases:|]}}],version:1}", "",
               re.sub("\\t|\\n| |\"|SpawnZombiesJitteredWaveActionProps|DinoWaveActionProps", "", waves_tmp2))))).split("|")
    waves.remove("")

    gi = ''
    level_name = ''
    if level_name_tmp:
        level_name = level_name_tmp.group(1)
    if full_level_name_tmp:
        full_level_name = full_level_name_tmp.group(1)
    if gi_tmp:
        gi = gi_tmp.group(1)
    if flag_count_tmp:
        flag_count = flag_count_tmp.group(1)
    if wave_format_tmp:
        wave_format = wave_format_tmp.group(1)

    before_level = level_name.split("-")
    before_level[1] = str(int(before_level[1]) - 1)
    before_level = "-".join(before_level)
    after_level = level_name.split("-")
    after_level[1] = str(int(after_level[1]) + 1)
    after_level = "-".join(after_level)

    new_waves = []
    for index in range(len(waves)):
        index += 1
        if index % 2 == 0:
            new_waves.append(re.sub('(\\d);({{P\\|\\S+\\s*\\S*\\|2}})<sup>0</sup>', '\\2<sup>\\1</sup>',
                                    re.sub('|AdditionalPlantfood\\d', '',
                                           re.sub("(<sup>\\d</sup>);(\\d+\\.*\\d*);({{P\\|.+?\\|2}})", "\\3\\1#\\2#",
                                                  re.sub("<sup>(\\d)</sup>;<sup>0</sup>", "<sup>\\1</sup>", convert(
                                                      re.sub('\"AdditionalPlantfood\": 1,', '',
                                                             re.sub("(\\d)\\(", "<sup>\\1</sup>(",
                                                                    str(waves[index - 1]))))))))[:-1].split("#"))
        else:
            new_waves.append(re.sub("Wave", "", str(waves[index - 1])))

    tmp_list = f.tmp_list(new_waves)

    for i in range(len(tmp_list)):
        tmp_list[i - 1] = re.sub('<sup>\\d</sup>', "", tmp_list[i - 1])

    zmb_set = set(tmp_list)

    wave_format = re.sub('RTID|@CurrentLevel|\\)|\\(|Wave|]|\\[|\"| |\\n', "", wave_format).split(',')

    print(new_waves)

    # Sorts the zombies
    sorted_list = f.sort_zombies(new_waves)

    final_list = []
    for i in range(len(wave_format)):
        for o in range(len(sorted_list)):
            if o % 2 == 1:
                if wave_format[i - 1] == sorted_list[o - 1]:
                    final_list.append(sorted_list[o])

    final_list.append(final_list[0])
    final_list.pop(0)

    final_string = ""
    for item in range(len(final_list)):
        if ((item + 1) / int(re.search('\"WavesPerFlag\": (\\d+),\\n', file_data).group(1)) % 1) == 0.0:
            tmp = "Flag"
        else:
            tmp = "<br />"

        if item == len(final_list) - 1:
            tmp2 = "}"
        else:
            tmp2 = "-"

        final_string += f'|{item + 1}\n|'
        for i in range(len(final_list[item])):
            final_string += f'{final_list[item][i][0]} '
        if ((item + 1) / int(re.search('\"WavesPerFlag\": (\\d+),\\n', file_data).group(1)) % 1) == 0.0:
            final_string += '{{P|Flag Zombie|2}}'
        final_string += '\n|None\n'
        final_string += f'|{tmp}\n'
        final_string += f'|{tmp2}\n'

    # For dist use:
    # f.openUrl('https://project-eclise.fandom.com/wiki/{}(Alpha)?action=edit'.format(level_name))

    # For debug use:
    # print(f'opened https://project-eclise.fandom.com/wiki/{level_name}(Alpha)?action=edit')

    gravestone_count = gi.count("gravestone_egypt" or "gravestone_dark" or "gravestoneSunOnDestruction")
    no_numb_lvl_name = re.sub("\\d+?-\\d+: ", "", full_level_name)

    final_string = """{{{{BAHTabber|Level={}}}}}
{{{{Level Infobox
|name = {}
|image = {}Alpha.jpg
|Type = Regular
|EM = {}
|Flag = {}
|Plant = Choice
|Zombie = {}
|FR =
|NR =
|before = {} (Alpha)
|after = {} (Alpha)
}}}}
\'\'\'{}\'\'\', also known as \'\'\'{}\'\'\'

{{{{clear}}}}
== Waves ==
{{| class="article-table"
!Waves
!Non-dynamic zombies
!Ambush zombies
!Notes
|-
{}

==Gallery==
<br />{{LevelsA}}
""".format(level_name, full_level_name, level_name, gravestone_count, flag_count,
           ' '.join(zmb_set) + ' {{P|Flag Zombie|2}}', before_level, after_level, no_numb_lvl_name, level_name,
           final_string)

    f.final_click(final_string)


if __name__ == '__main__':
    main('tmp.json')
