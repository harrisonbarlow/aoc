def find_new(sequence):
    if all([i == 0 for i in sequence]):
        return 0
    
    return sequence[-1] + find_new([j - i for i, j in zip(sequence, sequence[1:])])


def find_old(sequence):
    if all([i == 0 for i in sequence]):
        return 0
    
    return sequence[0] - find_old([j - i for i, j in zip(sequence, sequence[1:])])


def solve(sequences, finder):
    return sum([finder(sequence) for sequence in sequences])


def main():
    sequences = [list(map(int, line.split())) for line in open('input.txt').readlines()]

    print(solve(sequences, find_new))
    print(solve(sequences, find_old))


if __name__ == '__main__':
    main()