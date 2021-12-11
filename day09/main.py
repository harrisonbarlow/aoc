import math

searched = dict()

def find_basin_size(heights, x, y):
    if heights[y][x] != 9 and f"{x},{y}" not in searched:
        searched[f"{x},{y}"] = True
        return 1 + find_basin_size(heights, x, y-1) + find_basin_size(heights, x, y+1) + find_basin_size(heights, x-1, y) + find_basin_size(heights, x+1, y)
    else:
        return 0


def solve2(heights):
    sizes = set()
    
    for y in range(1, len(heights) -1):
        for x in range(1, len(heights[y]) - 1):
            sizes.add(find_basin_size(heights, x, y))
    
    return math.prod(list(sizes)[-3:])


def solve1(heights):
    low = []

    for y in range(1, len(heights) - 1):
        for x in range(1, len(heights[y]) - 1):
            val = heights[y][x]

            if val < heights[y-1][x] and val < heights[y+1][x] and val < heights[y][x-1] and val < heights[y][x+1]:
                low.append(val)

    risk = 0
    for point in low:
        risk += point + 1

    return risk

def pad(array, pad):
    newarray = []

    for line in array:
        newarray.append([pad] + [int(c) for c in line] + [pad])

    xlen = len(newarray[0])
    row = [pad] * xlen
    newarray = [row] + newarray + [row]

    return newarray


def main():
    heights = list(map(list, open("input.txt").read().rstrip().split("\n")))

    print(solve1(pad(heights, 10)))
    print(solve2(pad(heights, 9)))


if __name__ == "__main__":
    main()