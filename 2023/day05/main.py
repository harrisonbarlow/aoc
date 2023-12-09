from functools import reduce
from itertools import count

def chain(start, *funcs):
    return reduce(lambda res, func: func(res), funcs, start)


def mapper(map):
    def func(number):
        for destination, source, length in map:
            if source <= number < source + length:
                return destination + number - source
            
        return number

    return func


def solve2(seeds, *maps):
    for location in count():
        possible_seed = chain(location, *maps)

        for seed, num in zip(seeds[::2], seeds[1::2]):
            if seed <= possible_seed < seed + num:
                return location


def solve1(seeds, *maps):
    return min([chain(seed, *maps) for seed in seeds])


def main():
    seeds, *maps = open('input.txt').read().split('\n\n')

    seeds = [int(num) for num in seeds.split(': ')[1].split()]

    forward = [
        mapper([
            [int(d), int(s), int(l)] 
            for (d, s, l) in 
            [line.split() for line in chunk.splitlines()[1:]]
        ])
        for chunk in maps
    ]

    reverse = [
        mapper([
            [int(s), int(d), int(l)] 
            for (d, s, l) in 
            [line.split() for line in chunk.splitlines()[1:]]
        ])
        for chunk in reversed(maps)
    ]

    print(solve1(seeds, *forward))
    print(solve2(seeds, *reverse))


if __name__ == '__main__':
    main()