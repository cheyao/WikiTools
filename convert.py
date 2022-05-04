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
    ordered_list = [(x, int(y)) for x, y, in zip(mylist[::2], mylist[1::2])]
    sorted_list = sum([[x, str(y)] for x, y, in sorted(ordered_list, key=lambda x:x[1])], [])
    print(sorted_list)
