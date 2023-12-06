from math import prod
from functools import reduce


def solve(races):
    return prod([
        reduce(
            lambda acc, t: acc + 1 if t * (time - t) > distance else acc,
            range(0, time + 1),
            0
        )
        for time, distance in races
    ]) 


def main():
    time, distance = open('input.txt').read().split('\n')

    races = zip(map(int, time.split()[1:]), map(int, distance.split()[1:]))

    time = int(time.split(':')[1].replace(' ', ''))
    distance = int(distance.split(':')[1].replace(' ', ''))

    print(solve(races))
    print(solve([(time, distance)]))


if __name__ == '__main__':
    main()