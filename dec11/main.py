from time import sleep

def pad(array, pad):
    newarray = []

    for line in array:
        newarray.append([pad] + [int(c) for c in line] + [pad])

    xlen = len(newarray[0])
    row = [pad] * xlen
    newarray = [row] + newarray + [row]

    return newarray


def contains_flashes(octo, flashed):
    for y in range(1, len(octo) - 1):
        for x in range(1, len(octo[y]) - 1):
            if octo[y][x] > 9 and (y,x) not in flashed:
                return True

    return False

def solve2(octo):
    step = 1

    while True:

        flashed = dict()
        for y in range(1, len(octo) - 1):
            for x in range(1, len(octo[y]) - 1):
                octo[y][x] += 1

        while contains_flashes(octo, flashed):
            for y in range(1, len(octo) - 1):
                for x in range(1, len(octo[y]) - 1):
                    if(octo[y][x] > 9 and (y,x) not in flashed):
                        #octo[y][x] = 0
                        flashed[(y,x)] = True

                        octo[y-1][x] += 1
                        octo[y+1][x] += 1
                        octo[y][x-1] += 1
                        octo[y][x+1] += 1
                        octo[y-1][x-1] += 1
                        octo[y-1][x+1] += 1
                        octo[y+1][x-1] += 1
                        octo[y+1][x+1] += 1

        for y in range(1, len(octo) - 1):
            for x in range(1, len(octo[y]) - 1):
                if octo[y][x] > 9:
                    octo[y][x] = 0

        if len(flashed.keys()) == 100:
            print(octo)
            break

        step += 1

    return step


def solve1(octo, steps):

    counter = 0

    for s in range(steps):

        flashed = dict()
        for y in range(1, len(octo) - 1):
            for x in range(1, len(octo[y]) - 1):
                octo[y][x] += 1

        while contains_flashes(octo, flashed):
            for y in range(1, len(octo) - 1):
                for x in range(1, len(octo[y]) - 1):
                    if(octo[y][x] > 9 and (y,x) not in flashed):
                        flashed[(y,x)] = True

                        octo[y-1][x] += 1
                        octo[y+1][x] += 1
                        octo[y][x-1] += 1
                        octo[y][x+1] += 1
                        octo[y-1][x-1] += 1
                        octo[y-1][x+1] += 1
                        octo[y+1][x-1] += 1
                        octo[y+1][x+1] += 1

        for y in range(1, len(octo) - 1):
            for x in range(1, len(octo[y]) - 1):
                if octo[y][x] > 9:
                    octo[y][x] = 0
                    counter += 1

    return counter


def main():
    octo = [[int(x) for x in y] for y in [z.rstrip() for z in open("input.txt").readlines()]]

    print(solve1(pad(octo, 0), 100))
    print(solve2(pad(octo, 0)))

if __name__ == "__main__":
    main()