def find_max(lines):
    max_x = 0
    max_y = 0

    for line in lines:
        if line[0][0] > max_x:
            max_x = line[0][0]
        if line[1][0] > max_x:
            max_x = line[1][0]
        if line[0][1] > max_y:
            max_y = line[0][1]
        if line[1][1] > max_y:
            max_x = line[1][1]

    return max_x + 2, max_y + 2


def solve1(lines):
    max_x, max_y = find_max(lines)
    plane = [ [0] * max_x for _ in range(max_y) ]

    for line in lines:
        pfrom = line[0]
        pto = line[1]

        pfrom_x = pfrom[0]
        pfrom_y = pfrom[1]

        pto_x = pto[0]
        pto_y = pto[1]

        min_x = min(pfrom_x, pto_x)
        max_x = max(pfrom_x, pto_x)
        min_y = min(pfrom_y, pto_y)
        max_y = max(pfrom_y, pto_y)

        print(f"Drawing: ({pfrom_x}, {pfrom_y}) to ({pto_x}, {pto_y})")

        if pfrom_x == pto_x:
            for y in range(min_y, max_y + 1):
                plane[y][pfrom_x] += 1

        if pfrom_y == pto_y:
            for x in range(min_x, max_x + 1):
                plane[pfrom_y][x] += 1
        
        if pfrom_x != pto_x and pfrom_y != pto_y:
            if pfrom_x < pto_x:
                if pfrom_y > pto_y:
                    print('1')
                    for i in range(max_y - min_y + 1):
                        plane[pfrom_y - i][pfrom_x + i] += 1
                else:
                    print('2')
                    for i in range(max_y - min_y + 1):
                        plane[pfrom_y + i][pfrom_x + i] += 1
            elif pfrom_x > pto_x:
                if pfrom_y > pto_y:
                    for i in range(max_y - min_y + 1):
                        plane[pfrom_y - i][pfrom_x - i] += 1
                else:
                    for i in range(max_y - min_y + 1):
                        plane[pfrom_y + i][pfrom_x - i] += 1

        # for line in plane:
        #     print(line)


    counter = 0

    for y in plane:
        for x in y:
            if x >= 2:
                counter += 1

    #print(plane)
    print(counter)

def main():
    lines = []
    for line in open("input.txt"):
        trimmed = line.rstrip()
        trimmed = trimmed.replace(' ', '')
        points = trimmed.split('->')
        
        point_from = points[0].split(',')
        point_to = points[1].split(',')

        lines.append([(int(point_from[0]), int(point_from[1])), (int(point_to[0]), int(point_to[1]))])

    solve1(lines)

if __name__ == "__main__":
    main()