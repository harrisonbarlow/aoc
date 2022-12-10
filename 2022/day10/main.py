
def solve2(input):
    x = 1
    hpos = 0
    cycle = 0
    display = ''
    ticks = {
        'noop': 1,
        'addx': 2
    }

    for instruction in input:
        for _ in range(ticks[instruction[0]]):
            display += '.' if abs(hpos - x) > 1 else '#'

            cycle += 1
            hpos = cycle % 40

            if hpos == 0:
                display += '\n'

        if instruction[0] == 'addx':
            x += int(instruction[1])

    return display



def solve1(input):
    x = 1
    cycle = 0
    strengths = []
    ticks = {
        'noop': 1,
        'addx': 2
    }

    for instruction in input:
        for _ in range(ticks[instruction[0]]):
            cycle += 1

            if cycle % 20 == 0:
                strengths.append(cycle * x)

        if instruction[0] == 'addx':
            x += int(instruction[1])

    return sum(strengths[0::2])


def main():
    input = ([line.split() for line in open('input.txt').readlines()])

    print(solve1(input))
    print(solve2(input))

if __name__ == "__main__":
    main()