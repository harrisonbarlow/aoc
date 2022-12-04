
scores_1 = {
    "A": {
        "X": 1 + 3,
        "Y": 2 + 6,
        "Z": 3 + 0,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6
    },
    "C": {
        "X": 1 + 6,
        "Y": 2 + 0,
        "Z": 3 + 3
    },
}

scores_2 = {
    "A": {
        "A": 1 + 3,
        "B": 2 + 6,
        "C": 3 + 0,
    },
    "B": {
        "A": 1 + 0,
        "B": 2 + 3,
        "C": 3 + 6
    },
    "C": {
        "A": 1 + 6,
        "B": 2 + 0,
        "C": 3 + 3
    },
}

wld = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B",
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    },
}


def main():
    strategy = [line.rstrip().split(" ") for line in open("input.txt").readlines()]

    score1 = 0
    score2 = 0

    for round in strategy:
        #score1 += scores_1[round[0]][round[1]]

        #score2 += scores_2[round[0]][wld[round[0]][round[1]]]

        match round[0]:
            case "A":
                match round[1]:
                    case "X":
                        score1 += 4
                        score2 += 3
                    case "Y":
                        score1 += 8
                        score2 += 4
                    case "Z":
                        score1 += 3
                        score2 += 8
            case "B":
                match round[1]:
                    case "X":
                        score1 += 1
                        score2 += 1
                    case "Y":
                        score1 += 5
                        score2 += 5
                    case "Z":
                        score1 += 9
                        score2 += 9
            case "C":
                match round[1]:
                    case "X":
                        score1 += 7
                        score2 += 2
                    case "Y":
                        score1 += 2
                        score2 += 6
                    case "Z":
                        score1 += 6
                        score2 += 7

    print(score1)
    print(score2)


if __name__ == "__main__":
    main()