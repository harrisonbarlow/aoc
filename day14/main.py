from collections import defaultdict
from time import perf_counter

def find_max(array):
    m = max(set(array), key=array.count)
    return array.count(m)


def find_min(array):
    m = min(set(array), key=array.count)
    return array.count(m)


def solve1(template, rules, steps):
    for _ in range(steps):
        new_template = []
        for i, _ in enumerate(list(template)):
            if i == 0:
                continue

            rule = rules[template[i-1] + template[i]]
            new_template += [template[i-1], rule]

        template = new_template + [template[-1]]

    return find_max(template) - find_min(template)


def solve(template, rules, steps):
    pair_counts = defaultdict(int)
    letter_counts = defaultdict(int)
    
    for i in range(1, len(template)):
        pair_counts[template[i - 1] + template[i]] += 1

    for _ in range(steps):
        new_pair_counts = defaultdict(int)

        for pairs, count in pair_counts.items():
            insert = rules[pairs]

            new_pair_counts[pairs[0] + insert] += count
            new_pair_counts[insert + pairs[1]] += count

        pair_counts = new_pair_counts

    for pairs, count in pair_counts.items():
        first = pairs[0]
        letter_counts[first] += count

    return max(letter_counts.values()) -  min(letter_counts.values()) + 1


def main():
    rules = dict()
    for index, line in enumerate(open("input.txt").readlines()):
        if index == 0:
            template = list(line.rstrip())
            continue
        if line == "\n":
            continue
        
        rule = line.rstrip().split(" -> ")
        rules[rule[0]] = rule[1]

    print(solve(template, rules, 10))
    print(solve(template, rules, 40))

if __name__ == "__main__":
    main()