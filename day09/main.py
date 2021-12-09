
def solve2(heights):
    pass


def solve1(heights):
    low = []
    print(heights)
    for y in range(1, len(heights) - 1):
        for x in range(1, len(heights[y]) - 1):
            val = heights[y][x]

            if val < heights[y-1][x] and val < heights[y+1][x] and val < heights[y][x-1] and val < heights[y][x+1]:
                low.append(val)

    risk = 0
    for point in low:
        risk += point + 1

    return risk


def main():
    #heights = list(map(list, open("input.txt").read().rstrip().split("\n")))
    heights = open("input2.txt").read().rstrip().split("\n")
    padded = []
    for height in heights:
        parsed = list(map(int, height))
        line = [10] + parsed + [10]
        padded.append(line)

    padded = [[10] * len(padded[0])] + padded + [[10] * len(padded[0])]

    print(solve1(padded))

if __name__ == "__main__":
    main()