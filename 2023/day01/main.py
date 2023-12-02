import re
import math

def solve2(input):
    number_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    calibrations = []

    for line in input:
        highest_index, lowest_index = -1, math.inf
        highest, lowest = None, None

        for sub in number_map:
            left = min(line.find(sub), line.rfind(sub))
            right = max(line.find(sub), line.rfind(sub))

            if left == -1 and right == -1:
                continue

            if left < lowest_index:
                lowest_index = left
                lowest = number_map[sub]

            if right > highest_index:
                highest_index = right
                highest = number_map[sub]

        calibrations.append(int(f"{lowest}{highest}"))

    return sum(calibrations)


def solve1(input):
    ints = lambda line: re.findall(r'\d', line)

    return sum(
        [
            int(f"{ints(line)[0]}{ints(line)[-1]}") 
            for line in input
        ]
    )


def main():
    input = [line.rstrip() for line in open("input.txt").readlines()]

    print(solve1(input))
    print(solve2(input))


if __name__ == "__main__":
    main()