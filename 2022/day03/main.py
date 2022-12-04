priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve1(rucksacks):
    sum = 0

    for rucksack in rucksacks:
        c1, c2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

        common = set(c1).intersection(c2)

        sum += priorities.find(common.pop()) + 1

    return sum

def solve2(rucksacks):
    sum = 0
    common = set()

    for rucksack in rucksacks:
        if len(common) == 0:
            common = set(rucksack)
        else:
            common = common.intersection(rucksack)

            if len(common) == 1:
                sum += priorities.find(common.pop()) + 1

    return sum


def main():
    rucksacks = [line.rstrip() for line in open("input.txt")]

    print(solve1(rucksacks))
    print(solve2(rucksacks))


if __name__ == "__main__":
    main()