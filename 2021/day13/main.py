from time import sleep

def count_hash(grid):
    counter = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "#":
                counter += 1

    return counter


def solve(coords, folds, first=False):
    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])

    grid = [['.'] * (max_x + 1) for _ in range(max_y + 1)]

    for [x, y] in coords:
        grid[y][x] = '#'

    for [axis, num] in folds:
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if axis == 'x' and x > int(num) and grid[y][x] == '#':
                    grid[y][int(num) - (x - int(num))] = '#'
                    grid[y][x] = '.'
                elif axis == 'y' and y > int(num) and grid[y][x] == '#':
                    grid[int(num) - (y - int(num))][x] = '#'
                    grid[y][x] = '.'

        if first:
            num_hashes = count_hash(grid)
            print(num_hashes)
            break
        else:
            continue
    
    if not first:
        for l in range(0, 6):
            print(grid[l][0:40])


def main():
    coords = []
    folds = []
    for line in open("input.txt").readlines():
        if line == "\n":
            continue
        if "fold" not in line:
            coords.append([int(pos) for pos in line.rstrip().split(',')])
        else:
            folds.append(line.rstrip().split()[2].split('='))

    solve(coords, folds, first=True)
    solve(coords, folds, first=False)


if __name__ == "__main__":
    main()