from functools import reduce

def chain(start, *funcs):
    return reduce(lambda res, func: func(res), funcs, start)


def mapper(map):
    def func(number):
        for destination, source, length in map:
            if source <= number <= source + length:
                return destination + (number - source)
            
        return number

    return func


def solve2(seeds, *maps):
    values = []
    for i in range(0, len(seeds), 2):
        seed = seeds[i]
        count = seeds[i + 1]

        for j in range(seed, seed + count):
             values.append(chain(seed, *maps))

    return min(values)


def solve1(seeds, *maps):
    return min([chain(seed, *maps) for seed in seeds])


def main():
    seeds, maps = [], []

    seeds, *maps = open('input.txt').read().split('\n\n')

    seeds = [int(num) for num in seeds.split(': ')[1].split()]

    maps = [
        mapper([
            [int(num) for num in line.split()]
            for line in chunk.splitlines()[1:]
        ])
        for chunk in maps
    ]

    print(solve1(seeds, *maps))
    print(solve2(seeds, *maps))


if __name__ == '__main__':
    main()