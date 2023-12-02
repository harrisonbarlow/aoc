from collections import defaultdict
from math import prod

def solve2(input):
    return sum([
        prod([
            max([bag[key] for bag in bags])
            for key in ['red', 'blue', 'green']
        ])
        for bags in input.values()
    ])


def solve1(input):
    limit = {'red': 12, 'green': 13, 'blue': 14}

    possible_games = []

    for game, bags in input.items():
        for bag in bags:
            for colour, count in bag.items():
                if count > limit[colour]:
                    break
            else:
                continue
            break
        else:
            possible_games.append(game)

    return sum(possible_games)


def main():
    lines = [input.rstrip('\n') for input in open('input.txt')]

    games = defaultdict(list)

    for index, line in enumerate(lines):
        for bag in line.split(': ')[1].split('; '):
            games[index + 1].append(
                defaultdict(int, {
                    result[1]: int(result[0])
                    for result in [
                        game.split(' ') 
                        for game in bag.split(', ')
                    ]
                })
            )

    print(solve1(games))
    print(solve2(games))


if __name__ == '__main__':
    main()