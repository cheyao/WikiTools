import json
import re
import convert as c
import itertools
import functions as fun

if __name__ == '__main__':
    f = open('tmp.json', 'r')
    json_file = json.load(f)
    final_string = ''

    name = json_file['objects'][0]['objdata']['Name']
    name_number = json_file['#comment']

    first = int(name_number.split('-')[0])
    second = int(name_number.split('-')[1])

    if second - 1 == 0 or 10 or 20:
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
        if item['aliases'] == i:
            unsorted_list.append(i[0])
            tmp_list = []
            for zombie in item['objdata']['Zombies']:
                converted_zombie = c.convert(re.sub('RTID\\(([\s\S]+?)@ZombieTypes\\)', '(\\1)', zombie['Type']))
                try:
                    row = zombie['Row']
                except KeyError:
                    row = '0'

                tmp_list2 = f'{converted_zombie}<sup>{row}</sup> '.split(";")
                tmp_list.append(tmp_list2[1])
                tmp_list.append(tmp_list2[0])
            unsorted_list.append(tmp_list)

    sorted_list = fun.sort_zombies(unsorted_list)

    print(sorted_list)
