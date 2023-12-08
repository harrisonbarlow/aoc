from dataclasses import dataclass
from collections import Counter


@dataclass
class Hand:
    hand: str
    bid: int
    card = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }

    @property
    def count(self):
        return Counter(self.hand)
    
    def __lt__(self, other):
        for c1, c2 in zip(self.count.most_common(), other.count.most_common()):
            if c1[1] < c2[1]:
                return True
            if c1[1] > c2[1]:
                return False
            
        for c1, c2 in zip(self.hand, other.hand):
            if self.card[c1] < self.card[c2]:
                return True
            if self.card[c1] > self.card[c2]:
                return False
            
class WildcardHand(Hand):
    @property
    def wildcard_count(self):
        return Counter(self.wildcard)
    
    @property
    def wildcard(self):
        if not 'J' in self.hand:
            return self.hand
        
        most_common = self.count.most_common()
        
        if len(most_common) == 1:
            return 'AAAAA'
        
        if most_common[0][0] == 'J':
            return self.hand.replace('J', most_common[1][0])

        return self.hand.replace('J', most_common[0][0])
    
    def __lt__(self, other):
        self.card['J'] = 1

        for c1, c2 in zip(self.wildcard_count.most_common(), other.wildcard_count.most_common()):
            if c1[1] < c2[1]:
                return True
            if c1[1] > c2[1]:
                return False
            
        for c1, c2 in zip(self.hand, other.hand):
            if self.card[c1] < self.card[c2]:
                return True
            if self.card[c1] > self.card[c2]:
                return False


def solve(hands):
    return sum([hand.bid * (i + 1) for i, hand in enumerate(sorted(hands))])


def main():
    hands = [Hand(hand, int(bid)) for hand, bid in [line.split() for line in open('input2.txt').read().splitlines()]]

    wildcard_hands = [WildcardHand(hand, int(bid)) for hand, bid in [line.split() for line in open('input2.txt').read().splitlines()]]

    print(solve(hands))
    print(solve(wildcard_hands))


if __name__ == '__main__':
    main()