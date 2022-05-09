import traceback
from tkinter import *
import json
import re
import itertools
import functions as fun


def convert(file="ALPHA3/adventure/Pirate16.json"):  # file is for debugging
    try:
        # Loads the level file
        f = open(file, 'r')
        json_file = json.load(f)

        # Gets a few vals from the level file
        template = ''.join(open('template.txt', 'r').readlines()[7:])
        link = ''.join(open('template.txt', 'r').readlines()[1:2])[:-1]
        name = json_file['objects'][0]['objdata']['Name']
        name_number = json_file['#comment']
        first_reward = json_file['objects'][0]['objdata']['FirstRewardParam'].capitalize()
        if first_reward == "big_moneybag":
            first_reward = ""
        replay_reward = ''

        # Gets the level's following and previous levels
        first = int(name_number.split('-')[0])
        second = int(name_number.split('-')[1])
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

        # Removes first item from the jsonfile
        json_file = json_file['objects']
        json_file.remove(json_file[0])

        # Some null safety values
        flags = 1
        waves_per_flag = 10
        wave_count = 10

        # Gets the waves order from WaveManager
        for item in json_file:
            if item['aliases'] == ["WaveManager"]:
                wave_count = len(item['objdata']["Waves"])
                try:
                    waves_per_flag = item['objdata']["FlagWaveInterval"]
                except KeyError:
                    waves_per_flag = 10
                flags = wave_count // waves_per_flag

        num_items_on_map = 0
        try:
            for i in json_file:
                if i['aliases'] == ['GI']:
                    num_items_on_map = len(i['objdata']['InitialGridItemPlacements'])
        except KeyError:
            num_items_on_map = 0
        plants = []
        try:
            for i in json_file:
                if i['aliases'] == ["SeedBank"]:
                    for plant in i['objdata']['PresetPlantList']:
                        plants.append(plant['PlantType'])
                    plants = ', '.join(plants)
        except KeyError:
            plants = 'Chooser'

        wave_list = []
        for item in json_file:
            if item['aliases'] == ["WaveManager"]:
                for i in item['objdata']["Waves"]:
                    for item2 in i:
                        wave_list.append(re.sub('RTID\\(([\s\S]+?)@CurrentLevel\\)', '\\1', item2))

        unsorted_list = []
        for i, item in itertools.product(wave_list, json_file):
            item_val = item['aliases'][0]
            if item_val == i:
                unsorted_list.append(i)
                tmp_list = []
                if re.match(r'RP\d+', item['aliases'][0]):
                    for il in range(item['objdata']['GroupSize'] * item['objdata']['SwashbucklerCount']):
                        tmp_list.append('{{P|Swashbuckler Zombie|2}}')
                        tmp_list.append('55')
                elif re.match(r'PR\d+', item['aliases'][0]):
                    for il in range(item['objdata']['GroupSize'] * item['objdata']['SpiderCount']):
                        tmp_list.append('{{P|Lost Pilot Zombie|2}}')
                        tmp_list.append('26')
                elif re.match(r'Tide\d+', item['aliases'][0]):
                    print('', end='')  # Null
                elif re.match(r'LT\d+', item['aliases'][0]):
                    for il in range(item['objdata']['GroupSize'] * item['objdata']['ZombieCount']):
                        tmp_list.append('{{P|Some LT zomb|2}}')
                        tmp_list.append('1')
                elif re.match(
                        r'piano|ZombiePianoDefault|GR\d+|RascalsMessage|RM|DoubleWaveMessage|ModConveyor|Magmacream'
                        r'|TrapTileProps_1|TrapActivate|CHM|CHMessage',
                        item['aliases'][0]):
                    print('', end='')  # Null
                elif re.match(r'Wave\d+P\d+', item['aliases'][0]):
                    tmp_list.append('{{P|PortalFF|2}}')
                    tmp_list.append(item['PortalRow'] + 1)
                elif re.match(r'L\d+[LR]Wind', item['aliases'][0]):
                    tmp_list.append('Wind')
                    tmp_list.append(item['objdata']['Winds']['Row'] + 1)
                else:
                    for zombie in item['objdata']['Zombies']:
                        converted_zombie1 = fun.convert(
                            re.sub('RTID\\(([\s\S]+?)@ZombieTypes\\)', '(\\1)', zombie['Type'] or zombie['DinoType']))
                        try:
                            tmp1 = zombie['Row'] or zombie['DinoRow']
                            row1 = f'<sup>{tmp1}</sup>'
                        except KeyError:
                            row1 = ''

                        tmp_list21 = f'{converted_zombie1}{row1} '.split(";")
                        tmp_list.append(tmp_list21[1])
                        tmp_list.append(tmp_list21[0])

                unsorted_list.append(tmp_list)
        print(unsorted_list)
        sorted_list = fun.sort_zombies(unsorted_list)

        zombie_waves = ''
        tmp_wave = 0
        for i in range(len(sorted_list)):
            if i % 2 != 0:
                if re.match('Wave\\d', sorted_list[i - 1]):
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
                                       zombie_waves=zombie_waves, first_reward=first_reward,
                                       replay_reward=replay_reward)

        link = link.format(name=name, before_name=before_name, after_name=after_name, zombies=zombies,
                           plants=plants, name_number=name_number, num_items_on_map=num_items_on_map,
                           flags=flags, waves_per_flag=waves_per_flag, wave_count=wave_count,
                           zombie_waves=zombie_waves, first_reward=first_reward, replay_reward=replay_reward)

        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(final_string)
        r.update()
        print(final_string)

        fun.openUrl(link)

        return True
    except:
        fun.error(traceback.format_exc(), file)
        print(traceback.format_exc())
        return False


if __name__ == '__main__':
    fun.show_window()
