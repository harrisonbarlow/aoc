from math import prod
from functools import cmp_to_key

def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                if (r := compare(l, r)) != 0:
                    return r
            return compare(len(left), len(right))
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])


def solve1(packets):
    indices = []
    for index, (left, right) in enumerate(zip(packets[::2], packets[1::2])):
        if compare(left, right) < 0:
            indices.append(index + 1)

    return sum(indices)


def solve2(packets):
    indices = []
    divider = [[[2]], [[6]]]

    for index, packet in enumerate(sorted(divider + packets, key=cmp_to_key(compare))):
        if packet in divider:
            indices.append(index + 1)

    return prod(indices)


def main():
    packets = [eval(line) for line in open('input.txt').read().splitlines() if len(line)]

    print(solve1(packets))
    print(solve2(packets))


if __name__ == "__main__":
    main()