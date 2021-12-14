from collections import defaultdict
from time import sleep

def find_max(array):
    m = max(set(array), key=array.count)

    return array.count(m)


def find_min(array):
    m = min(set(array), key=array.count)

    return array.count(m)


def solve2(template, rules, steps):
    counts = defaultdict(int)
    
    for i in range(len(template)):
        if i == 0:
            continue

        counts[template[i - 1] + template[i]] += 1

    for _ in range(steps):

        print(counts)

        newcounts = defaultdict(int)

        for pairs in list(counts.keys()):
            val = counts[pairs]
            char = rules[pairs]

            newcounts[pairs[0] + char] += val
            newcounts[char + pairs[1]] += val

        counts = newcounts

    histogram = defaultdict(int)

    for count in counts.keys():
        first = count[0]
        second = count[1]

        histogram[first] += counts[count]

    print(histogram)

    return (max(histogram.values()) -  min(histogram.values()) + 1)



def solve1(template, rules, steps):
    for _ in range(steps):
        #print(f"Step {_}: {template}")
        new_template = []
        for i, val in enumerate(list(template)):
            if i == 0:
                continue

            rule = rules[template[i-1] + template[i]]
            new_template += [template[i-1], rule]

        template = new_template + [template[-1]]

    return find_max(template) - find_min(template)


def main():
    template = ""
    rules = dict()
    for index, line in enumerate(open("input.txt").readlines()):
        if index == 0:
            template = list(line.rstrip())
            continue
        if line == "\n":
            continue
        

        rule = line.rstrip().split(" -> ")
        rules[rule[0]] = rule[1]

    #print(solve1(template, rules, 40))
    print(solve2(template, rules, 40))


if __name__ == "__main__":
    main()