def chain(start, *funcs):
    res = start
    for func in funcs:
        res = func(res)
    return res


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

        print(seed, count)

        # for j in range(seed, seed + count):
        values.append(chain(seed, *maps))

    return min(values)


def solve1(seeds, *maps):
    return min([chain(seed, *maps) for seed in seeds])


def main():
    seeds, maps = [], []
    
    for index, chunk in enumerate(open('input2.txt').read().split('\n\n')):
        if index == 0:
            seeds.extend([int(num) for num in chunk.split(': ')[1].split()])
            continue

        maps.append(
            mapper([
                [int(num) for num in line.split()]
                for line in chunk.splitlines()[1:]
            ])
        )

    print(solve1(seeds, *maps))
    print(solve2(seeds, *maps))


if __name__ == '__main__':
    main()