import traceback
from tkinter import *
import json
import re
import itertools
import functions as fun


def convert(file="ALPHA3/adventure/Pirate16.json"):  # filee value is for debugging
    # Error handling
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
        if second - 1 in (0, 10, 20):
            if second == 1:
                before_name = 'Null'
            elif first == 1:
                before_name = str(first + 11) + '-' + str(second - 10)
            else:
                before_name = str(first - 1) + '-' + str(second + 9)
        else:
            before_name = str(first) + '-' + str(second - 1)
        if second + 1 in (10, 20, 30):
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
                break

        # Gets number of items on map
        num_items_on_map = 0
        try:
            for i in json_file:
                if i['aliases'] == ['GI']:
                    num_items_on_map = len(i['objdata']['InitialGridItemPlacements'])
                    break
        except KeyError:
            num_items_on_map = 0

        # Gets the seedbank
        seed_bank = []
        try:
            for i in json_file:
                if i['aliases'] == ["SeedBank"]:
                    for plant in i['objdata']['PresetPlantList']:
                        seed_bank.append(plant['PlantType'])
                    seed_bank = ', '.join(seed_bank)
                    break
        except KeyError:
            seed_bank = 'Chooser'

        # Gets the waves from WaveManager
        wave_list = []
        for item in json_file:
            if item['aliases'] == ["WaveManager"]:
                for i in item['objdata']["Waves"]:
                    for item2 in i:
                        wave_list.append(re.sub('RTID\\(([\s\S]+?)@CurrentLevel\\)', '\\1', item2))
                break

        # Converts the waves in the WaveManager to wiki format
        unsorted_list = []
        for i, item in itertools.product(wave_list, json_file):

            item_val = item['aliases'][0]

            if item_val == i:

                unsorted_list.append(i)
                tmp_list = []

                if re.match(r'RP\d+', item['aliases'][0]):

                    for il in range(item['objdata']['GroupSize'] * item['objdata']['SwashbucklerCount']):
                        tmp_list.extend(['{{P|Swashbuckler Zombie|2}}', '55'])
                    unsorted_list.append(tmp_list)
                    continue
                elif re.match(r'PR\d+', item['aliases'][0]):

                    for il in range(item['objdata']['GroupSize'] * item['objdata']['SpiderCount']):
                        tmp_list.extend(['{{P|Lost Pilot Zombie|2}}', '26'])
                    unsorted_list.append(tmp_list)
                    continue
                elif re.match(r'LT\d+', item['aliases'][0]):

                    for il in range(item['objdata']['GroupSize'] * item['objdata']['ZombieCount']):
                        tmp_list.extend(['{{P|Some LT zomb|2}}', '1'])
                    unsorted_list.append(tmp_list)
                    continue
                elif re.match(
                        r'piano|ZombiePianoDefault|GR\d+|RascalsMessage|RM|DoubleWaveMessage|ModConveyor|Magmacream'
                        r'|TrapTileProps_1|TrapActivate|CHM|CHMessage|Tide\d+',
                        item['aliases'][0]):
                    continue
                elif re.match(r'Wave\d+P\d+', item['aliases'][0]):
                    tmp_list.extend(['{{P|PortalFF|2}}', item['PortalRow'] + 1])
                    unsorted_list.append(tmp_list)
                    continue
                elif re.match(r'L\d+[LR]Wind', item['aliases'][0]):
                    tmp_list.extend(['Wind', item['objdata']['Winds']['Row'] + 1])
                    unsorted_list.append(tmp_list)
                    continue
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
        # Sorts the waves
        sorted_list = fun.sort_zombies(unsorted_list)

        # Converts the sorted waves to wiki format with the wiki template
        zombie_waves = ''
        tmp_wave = 0
        for i in range(len(sorted_list))[::2]:
            if re.match('Wave\\d', sorted_list[i - 1]):

                tmp_wave += 1

                tmp = ' '.join(sorted_list[i][::2])

                zombie_waves += f'|{tmp_wave}\n|{tmp}'

                zombie_waves += '{{P|Flag Zombie|2}}\n' if tmp_wave % waves_per_flag == 0 else '\n|None\n'

                zombie_waves += '|Flag\n' if tmp_wave % waves_per_flag == 0 else '|<br />\n'

                zombie_waves += '|}\n' if tmp_wave == wave_count else '|-\n'
            else:
                tmp = ' '.join(sorted_list[i][::2])
                zombie_waves = re.sub('\\|None(\\n\\|(<br />)*(Flag)*\n\\|[-}])(?![\\S\\s]+\\|None\n\\|(<br />)*('
                                      'Flag)*\n\\|[-}])', f'|{tmp}\\1', zombie_waves)

        # Gets the num of zombies
        zombies = set()
        for item in range(len(sorted_list))[::2]:
            for i in sorted_list[item - 1][::2]:
                zombies.add(re.sub('<sup>\\d</sup>', '', i))

        zombies = '{{P|Flag Zombie|2}} ' + ''.join(zombies)

        # Formats the wiki template and link using the values
        final_string = template.format(name=name, before_name=before_name, after_name=after_name, zombies=zombies,
                                       seed_bank=seed_bank, name_number=name_number, num_items_on_map=num_items_on_map,
                                       flags=flags, waves_per_flag=waves_per_flag, wave_count=wave_count,
                                       zombie_waves=zombie_waves, first_reward=first_reward,
                                       replay_reward=replay_reward)

        link = link.format(name=name, before_name=before_name, after_name=after_name, zombies=zombies, seed_bank=seed_bank,
                           name_number=name_number, num_items_on_map=num_items_on_map, flags=flags,
                           waves_per_flag=waves_per_flag, wave_count=wave_count, zombie_waves=zombie_waves,
                           first_reward=first_reward, replay_reward=replay_reward)

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
