import re
import linecache


def convert(string: str) -> str:
    zombies_convert = open('convert.txt', 'r')

    for line in range(len([line.strip("\n") for line in zombies_convert if line != "\n"])):
        zombie = re.sub('\n', '', linecache.getline('convert.txt', line + 1)).split(': ')
        string = re.sub(str(zombie[0]), str(zombie[1]), string)

    return string


if __name__ == '__main__':
    mylist = ['Pizza', '1', 'Apple', 2, 'Pizza', '5', 'Orange', '50', 'Pear', '40']
    for i in mylist[::2]:
        print(i)
