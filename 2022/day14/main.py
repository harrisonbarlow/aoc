import sys
import numpy as np
from time import sleep
from copy import deepcopy

#np.set_printoptions(threshold=sys.maxsize, edgeitems=30, linewidth=100000)
sand_pos = (0, 500)


def move_sand(cave, y, x, max_y=None):
    if max_y is not None:
        if y > max_y:
            raise IndexError

    if cave[y+1, x] == '.':
        cave[y+1, x] = 'o'
        cave[y, x] = '.'
        return move_sand(cave, y+1, x, max_y=max_y)

    if cave[y+1, x-1] == '.':
        cave[y+1, x-1] = 'o'
        cave[y, x] = '.'

        return move_sand(cave, y+1, x-1, max_y=max_y)

    if cave[y+1, x+1] == '.':
        cave[y+1, x+1] = 'o'
        cave[y, x] = '.'

        return move_sand(cave, y+1, x+1, max_y=max_y)

    return cave


def solve1(cave, max_y):
    index = 0
    (y, x) = sand_pos

    while True:
        try:
            cave[y, x] = 'o'
            cave = move_sand(cave, y, x, max_y=max_y)
            index += 1
        except IndexError:
            break
    return index


def solve2(cave):
    index = 0
    (y, x) = sand_pos

    while True:
        cave[y, x] = 'o'
        index += 1
        cave = move_sand(cave, y, x)

        if cave[y, x] == 'o':
            break
        
    return index



def main():
    input = [line.split('->') for line in open('input.txt').read().splitlines()]

    cave = np.full((10000, 10000), '.')

    max_y = 0

    for path in input:
        for start, end in zip(path, path[1:]):
            start_x, start_y = map(int, start.split(','))
            end_x, end_y = map(int, end.split(','))

            if start_y > max_y or end_y > max_y:
                max_y = max(start_y, end_y)

            if start_x == end_x:
                cave[min(start_y, end_y):max(start_y, end_y) + 1, start_x] = '#'

            if start_y == end_y:
                cave[start_y, min(start_x, end_x):max(start_x, end_x) + 1,] = '#'


    cave[max_y + 2, :] = '#'

    print(solve1(deepcopy(cave), max_y))
    print(solve2(deepcopy(cave)))


if __name__ == "__main__":
    main()