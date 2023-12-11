def find(sequence):
    if all([i == 0 for i in sequence]):
        return 0
    
    return sequence[-1] + find([j - i for i, j in zip(sequence, sequence[1:])])


def solve2(sequences):
    return sum([find(list(reversed(sequence))) for sequence in sequences])


def solve1(sequences):
    return sum([find(sequence) for sequence in sequences])


def main():
    sequences = [list(map(int, line.split())) for line in open('input.txt').readlines()]

    print(solve1(sequences))
    print(solve2(sequences))


if __name__ == '__main__':
    main()