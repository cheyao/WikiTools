import json
import re
import convert as c

if __name__ == '__main__':
    f = open('tmp.json', 'r')
    json_file = json.load(f)

    name = json_file['objects'][0]['objdata']['Name']
    name_number = json_file['#comment']

    json_file_removed = json_file['objects']
    json_file_removed.remove(json_file_removed[0])

    wave_list = []
    for item in json_file_removed:
        if item['aliases'] == ["WaveManager"]:
            for i in item['objdata']["Waves"]:
                wave_list.append([re.sub('RTID\\(([\s\S]+?)@CurrentLevel\\)', '\\1', i[0])])

    for i in wave_list:
        for item in json_file_removed:
            item_val = item['aliases']
            if item['aliases'] == i:
                print(i[0])
                for zombie in item['objdata']['Zombies']:
                    converted_zombie = c.convert(re.sub('RTID\\(([\s\S]+?)@ZombieTypes\\)', '(\\1)', zombie['Type']))
                    print(converted_zombie + ' Row: ' + zombie['Row'])
