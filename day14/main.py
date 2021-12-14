from collections import defaultdict
from time import sleep

def find_max(array):
    m = max(set(array), key=array.count)

    return array.count(m)


def find_min(array):
    m = min(set(array), key=array.count)

    return array.count(m)

def solve1(template, rules, steps):
    for _ in range(steps):
        new_template = []
        for i, val in enumerate(list(template)):
            if i == 0:
                continue

            rule = rules[template[i-1] + template[i]]
            new_template += [template[i-1], rule]

        template = new_template + [template[-1]]

    return find_max(template) - find_min(template)


def solve(template, rules, steps):
    paircounts = defaultdict(int)
    lettercounts = defaultdict(int)
    
    for i in range(1, len(template)):
        paircounts[template[i - 1] + template[i]] += 1

    for _ in range(steps):
        newpaircounts = defaultdict(int)

        for pairs in list(paircounts.keys()):
            count = paircounts[pairs]
            insert = rules[pairs]

            newpaircounts[pairs[0] + insert] += count
            newpaircounts[insert + pairs[1]] += count

        paircounts = newpaircounts

    for count in paircounts.keys():
        first = count[0]
        lettercounts[first] += paircounts[count]

    return max(lettercounts.values()) -  min(lettercounts.values()) + 1


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