
def solve1(pairs):
    count = 0

    for p1, p2 in pairs:
        p1min, p1max = map(int, p1.split('-'))
        p2min, p2max = map(int, p2.split('-'))

        r1 = range(p1min, p1max + 1)
        r2 = range(p2min, p2max + 1)

        if set(r1).issubset(r2) or set(r2).issubset(r1):
            count += 1
    
    return count


def solve2(pairs):
    count = 0

    for p1, p2 in pairs:
        p1min, p1max = map(int, p1.split('-'))
        p2min, p2max = map(int, p2.split('-'))

        r1 = range(p1min, p1max + 1)
        r2 = range(p2min, p2max + 1)

        if set(r1).intersection(r2):
            count += 1
    
    return count


def main():
    pairs = [line.rstrip().split(',') for line in open("input.txt")]

    print(solve1(pairs))
    print(solve2(pairs))

if __name__ == "__main__":
    main()