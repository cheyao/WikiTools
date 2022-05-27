import json
import re
import webbrowser
from sys import platform
import pyperclip as copy
import functions as f


# Rewrite #5
def convert(path="tmp.json"):  # file value is for debugging
    # Boring stuff
    template = ''.join(open('template.txt', 'r').readlines()[7:])
    link = ''.join(open('template.txt', 'r').readlines()[1:2])[:-1]
    convert_template = json.load(open('convert.json', 'r'))
    file = json.load(open(path, 'r'))
    name_number = file["#comment"]
    objects = file["objects"]
    level_info = objects[0]["objdata"]
    name = level_info["Name"]
    before_name = name_number[:2] + str(int(name_number[2]) - 1)
    after_name = name_number[:2] + str(int(name_number[2]) + 1)
    seed_bank = objects[1]["objdata"]["SelectionMethod"]
    first_reward = level_info['FirstRewardParam']
    try:
        num_items_on_map = len(objects[2]["objdata"]["InitialGridItemPlacements"])
    except KeyError:
        num_items_on_map = 0
    objects = objects[1:]
    indexes = []
    for i in objects:
        indexes.append(i["aliases"])
    waves = objects[indexes.index(["WaveManager"])]['objdata']
    waves_per_flag = waves['FlagWaveInterval']
    wave_count = waves['WaveCount']
    flags = wave_count / waves_per_flag
    waves = waves['Waves']
    for i in range(len(waves)):
        waves[i - 1] = [re.sub('RTID\\((\\S*)@CurrentLevel\\)', '\\1', waves[i - 1][0])]

    # Main stuff
    _zombie_waves = []
    for i in objects:
        if i['aliases'] in waves:
            ls = []
            for j in i['objdata']['Zombies']:
                try:
                    ls.append('<sup>' + j['Row'] + '</sup>;' + re.sub('RTID\\(([\S\s]+?)@ZombieTypes\\)', '\\1',
                                                                      j['Type']))
                except KeyError:
                    ls.append('<sup>0</sup>;' + re.sub('RTID\\(([\S\s]+?)@ZombieTypes\\)', '\\1', j['Type']))
            _zombie_waves.append(ls)

    for i in range(len(_zombie_waves)):
        for j in range(len(_zombie_waves[i - 1])):
            tmp = _zombie_waves[i - 1][j - 1].split(';')
            _zombie_waves[i - 1][j - 1] = tmp[0] + ';' + convert_template[tmp[1]]
        _zombie_waves[i - 1].sort(key=lambda x: int(x.split('|')[-1]))
        for j in range(len(_zombie_waves[i - 1])):
            _zombie_waves[i - 1][j - 1] = _zombie_waves[i - 1][j - 1].split('}|')[0] + '}'

    zombies = []
    for i in range(len(_zombie_waves)):
        for j in _zombie_waves[i]:
            tmp = j.split(';')
            zombies.append(tmp[1])
    zombies = ', '.join(list(set(zombies)))

    zombie_waves = ''
    for i, w in zip(_zombie_waves, waves):
        tmp = re.sub('Wave', '', w[0])
        zombie_waves += f'|{tmp}\n|'
        try:
            if int(tmp) % int(waves_per_flag) == 0:
                zombie_waves += '{{P|Flag Zombie|2}} '
        except ValueError:
            pass
        for j in i:
            zombie_waves += j.split(';')[1] + j.split(';')[0] + ' '
        try:
            zombie_waves += '\n|None\n|Flag\n|-\n' if int(tmp) % int(waves_per_flag) == 0 else '\n|None\n|<br />\n|-\n'
        except ValueError:
            zombie_waves += '\n|None\n|<br />\n|-\n'

    # Last formatting
    final_string = template.format(name=name, before_name=before_name, after_name=after_name, zombies=zombies,
                                   seed_bank=seed_bank, name_number=name_number, num_items_on_map=num_items_on_map,
                                   flags=flags, waves_per_flag=waves_per_flag, wave_count=wave_count,
                                   zombie_waves=zombie_waves, first_reward=first_reward, wave_order=waves,
                                   replay_reward='')

    link = link.format(name=name, name_number=name_number)

    chrome_path = "null"
    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome %s'
    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    elif platform == "win32":
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    copy.copy(final_string)

    webbrowser.get(chrome_path).open(link)


if __name__ == '__main__':
    f.show_window()
