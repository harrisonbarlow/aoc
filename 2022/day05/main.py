from copy import deepcopy
from collections import defaultdict

def solve2(stacks, input_procedure):
    for procedure in input_procedure.split('\n'):
        _, move, _, fr, _, to = procedure.split(' ')

        temp = []

        for _ in range(int(move)):
            temp.append(stacks[fr].pop())
        
        stacks[to].extend(reversed(temp))

    return ''.join([stacks[stack][-1] for stack in stacks])


def solve1(stacks, input_procedure):
    for procedure in input_procedure.split('\n'):
        _, move, _, fr, _, to = procedure.split(' ')

        for _ in range(int(move)):
            stacks[to].append(stacks[fr].pop())

    return ''.join([stacks[stack][-1] for stack in stacks])


def main():
    with open('input.txt') as f:
        stacks_input, procedure = f.read().split('\n\n')

    stacks = defaultdict(list)
    
    for row in list(reversed(stacks_input.split('\n')))[1:]:
        for i in range(0, (len(row) // 4) + 1):
            j = i * 4 + 1

            if row[j] != ' ':
                stacks[str(i + 1)].append(row[j])

    print(solve1(deepcopy(stacks), procedure))
    print(solve2(deepcopy(stacks), procedure))


if __name__ == "__main__":
    main()