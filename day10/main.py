
def are_opposite(open, close):
    if open == '(' and close == ')':
        return True
    if open == '{' and close == '}':
        return True
    if open == '[' and close == ']':
        return True
    if open == '<' and close == '>':
        return True

    return False


def solve2(lines):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    opposites = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    scores = []

    for line in lines:
        current_open = []
        for char in line:
            match char:
                case ('['|'{'|'('|'<'):
                    current_open.append(char)
                case (']'|'}'|')'|'>'): 
                    popped = current_open.pop()

        complete = ""

        current_open.reverse()

        for char in current_open:
            complete += opposites[char]

        score = 0
        for c in complete:
            score = score * 5
            score += points[c]

        scores.append(score)
  
    scores.sort()

    middle = (len(scores) - 1) / 2

    return scores[int((len(scores) - 1) / 2)]

def solve1(lines):
    score = {
       ')': 3,
       ']': 57,
       '}': 1197,
       '>': 25137
    }

    total_score = 0
    invalid_lines = []

    for line in lines:
        current_open = []
        for char in line:
            match char:
                case ('['|'{'|'('|'<'):
                    current_open.append(char)
                case (']'|'}'|')'|'>'): 
                    popped = current_open.pop()
                    if not are_opposite(popped, char):
                        total_score += score[char]
                        invalid_lines.append(line)
                        break
                    else:
                        continue
                        
    return total_score, invalid_lines


def main():
    lines = [x.rstrip() for x in open("input.txt").readlines()]

    total_score, invalid_lines = solve1(lines)
    print(total_score)

    valid_lines = list(set(lines) - set(invalid_lines))

    print(solve2(valid_lines))

if __name__ == "__main__":
    main()