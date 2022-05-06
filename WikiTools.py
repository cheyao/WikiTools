from tkinter import *
import json
import re
import itertools
import functions as fun


def convert(file):
    f = open(file, 'r')
    json_file = json.load(f)

    template = ''.join(open('template.txt', 'r').readlines()[7:])
    link = ''.join(open('template.txt', 'r').readlines()[1:2])

    name = json_file['objects'][0]['objdata']['Name']
    name_number = json_file['#comment']
    first_reward = json_file['objects'][0]['objdata']['FirstRewardParam'].capitalize()
    if first_reward == "big_moneybag":
        first_reward = ""
    replay_reward = ''

    first = int(name_number.split('-')[0])
    second = int(name_number.split('-')[1])

    print(first, second, str(first) + '-' + str(second - 1))

    if second - 1 == 0 or second - 1 == 10 or second - 1 == 20:
        if second == 1:
            before_name = 'Null'
        elif first == 1:
            before_name = str(first + 11) + '-' + str(second - 10)
        else:
            before_name = str(first - 1) + '-' + str(second + 9)
    else:
        before_name = str(first) + '-' + str(second - 1)

    if second + 1 == 10 or second + 1 == 20 or second + 1 == 30:
        after_name = str(first + 1) + '-' + str(second - 8)
    else:
        after_name = str(first) + '-' + str(second + 1)

    json_file_removed = json_file['objects']
    json_file_removed.remove(json_file_removed[0])

    wave_list = []
    for item in json_file_removed:
        if item['aliases'] == ["WaveManager"]:
            for i in item['objdata']["Waves"]:
                wave_list.append([re.sub('RTID\\(([\s\S]+?)@CurrentLevel\\)', '\\1', i[0])])

    flags = 1
    waves_per_flag = 10
    wave_count = 10
    for item in json_file_removed:
        if item['aliases'] == ["WaveManager"]:
            wave_count = item['objdata']["WaveCount"]
            waves_per_flag = item['objdata']["FlagWaveInterval"]
            flags = wave_count // waves_per_flag

    num_items_on_map = 0
    try:
        for i in json_file_removed:
            if i['aliases'] == ['GI']:
                num_items_on_map = len(i['objdata']['InitialGridItemPlacements'])
    except KeyError:
        num_items_on_map = 0

    plants = []
    try:
        for i in json_file_removed:
            if i['aliases'] == ["SeedBank"]:
                for plant in i['objdata']['PresetPlantList']:
                    plants.append(plant['PlantType'])
                plants = ', '.join(plants)
    except KeyError:
        plants = 'Chooser'

    unsorted_list = []

    for i, item in itertools.product(wave_list, json_file_removed):
        item_val = item['aliases']
        if item_val == i:
            unsorted_list.append(i[0])
            tmp_list = []
            for zombie in item['objdata']['Zombies']:
                converted_zombie = fun.convert(re.sub('RTID\\(([\s\S]+?)@ZombieTypes\\)', '(\\1)', zombie['Type']))
                try:
                    row = zombie['Row']
                except KeyError:
                    row = '0'

                tmp_list2 = f'{converted_zombie}<sup>{row}</sup> '.split(";")
                tmp_list.append(tmp_list2[1])
                tmp_list.append(tmp_list2[0])
            unsorted_list.append(tmp_list)

    sorted_list = fun.sort_zombies(unsorted_list)

    zombie_waves = ''
    tmp_wave = 0
    for i in range(len(sorted_list)):
        if i % 2 != 0:
            if re.match(r'Wave\d', sorted_list[i - 1]):
                tmp_wave += 1
                tmp = sorted_list[i][::2]
                tmp = ' '.join(tmp)
                zombie_waves += f'|{tmp_wave}\n|{tmp}'

                if tmp_wave % waves_per_flag == 0:
                    zombie_waves += '{{P|Flag Zombie|2}}\n'
                else:
                    zombie_waves += '\n'
                zombie_waves += '|None\n'

                if tmp_wave % waves_per_flag == 0:
                    zombie_waves += '|Flag\n'
                else:
                    zombie_waves += '|<br />\n'

                if tmp_wave == wave_count:
                    zombie_waves += '|}\n'
                else:
                    zombie_waves += '|-\n'

            else:
                tmp = sorted_list[i][::2]
                tmp = ' '.join(tmp)

                zombie_waves = re.sub('\\|None(\\n\\|(<br />)*(Flag)*\n\\|[-}])(?![\\S\\s]+\\|None\n\\|(<br />)*('
                                      'Flag)*\n\\|[-}])', f'|{tmp}\\1', zombie_waves)

    zombies = set()
    for item in range(len(sorted_list)):
        if item % 2 == 0:
            for i in sorted_list[item - 1][::2]:
                zombies.add(re.sub('<sup>\\d</sup>', '', i))

    zombies = '{{P|Flag Zombie|2}} ' + ''.join(zombies)

    final_string = template.format(name=name, before_name=before_name, after_name=after_name, zombies=zombies,
                                   plants=plants, name_number=name_number, num_items_on_map=num_items_on_map,
                                   flags=flags, waves_per_flag=waves_per_flag, wave_count=wave_count,
                                   zombie_waves=zombie_waves, first_reward=first_reward, replay_reward=replay_reward)

    link = link.format(name=name, before_name=before_name, after_name=after_name, zombies=zombies,
                       plants=plants, name_number=name_number, num_items_on_map=num_items_on_map,
                       flags=flags, waves_per_flag=waves_per_flag, wave_count=wave_count,
                       zombie_waves=zombie_waves, first_reward=first_reward, replay_reward=replay_reward)

    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(final_string)
    r.update()
    fun.openUrl(link)

    return True


if __name__ == '__main__':
    fun.show_window()
