import re
import linecache


def convert(string: str) -> str:
    zombies_convert = open('convert.txt', 'r')

    for line in range(len([line.strip("\n") for line in zombies_convert if line != "\n"])):
        zombie = re.sub('\n', '', linecache.getline('convert.txt', line + 1)).split(': ')
        string = re.sub(str(zombie[0]), str(zombie[1]), string)

    return string
