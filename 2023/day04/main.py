import re
from dataclasses import dataclass


@dataclass
class Card:
    winning: set
    numbers: set
    count: int


def solve2(cards):
    for index, card in enumerate(cards):
        matching = card.winning & card.numbers

        for i in range(index + 1, index + len(matching) + 1):
            cards[i].count += card.count

    return sum([
        card.count
        for card in cards
    ])


def solve1(cards):
    return sum ([
        int(2 ** (len(card.winning & card.numbers) - 1))
        for card in cards
    ])


def main():
    lines = [input.rstrip('\n') for input in open('input.txt')]

    cards = [
        Card(
            { int(num) for num in re.findall(r'\d+', winning) },
            { int(num) for num in re.findall(r'\d+', numbers) },
            1
        )
        for winning, numbers in [
            line.split(':')[1].split(' | ')
            for line in lines
        ]
    ]

    print(solve1(cards))
    print(solve2(cards))


if __name__ == '__main__':
    main()