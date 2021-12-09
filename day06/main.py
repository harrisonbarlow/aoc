from collections import deque

def solve2(fish, time):
    groups = deque([0] * 9)

    for f in fish:
        groups[f] += 1

    for _d in range(time):
        groups.rotate(-1)
        groups[6] += groups[8]

    return sum(groups)


def solve1(fish, time):
    for _d in range(time):
        new = []
        for i, f in enumerate(fish):
            if fish[i] == 0:
                fish[i] = 6
                new.append(8)
            else:
                fish[i] = fish[i] - 1

        fish = fish + new
        new = []

    return len(fish)


def main():
    fish = list(map(int, open("input.txt").read().rstrip().split(",")))
    days = 256
    print(solve2(fish, days))

if __name__ == "__main__":
    main()