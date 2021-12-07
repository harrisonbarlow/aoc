import math


def triangle(n):
    return int((n**2 + n) / 2)

def solve2(positions):
    lowest = 999999999999

    for i in positions:
        sum = 0
        for j in positions:
            sum += triangle(abs(i - j))
        
        if sum < lowest:
            lowest = sum

    return lowest


def solve1(positions):
    lowest = 999999999999

    for i in positions:
        sum = 0
        for j in positions:
            sum += abs(i - j)
        
        if sum < lowest:
            lowest = sum

    return lowest


def main():
    positions = list(map(int, open("input.txt").read().rstrip().split(",")))
    print(solve2(positions))

if __name__ == "__main__":
    main()