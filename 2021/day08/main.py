import itertools


def solve1(outputs):
    counter = 0
    for output in outputs:
        if len(output) == 2:
            counter += 1
        if len(output) == 4:
            counter += 1
        if len(output) == 3:
            counter += 1
        if len(output) == 7:
            counter += 1

    return counter


def generate_possibilities():
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    possibilities = list(itertools.permutations(chars))

    return possibilities


def is_valid(inputs, configuration):
    mapping = {
        configuration[0]: '0',
        configuration[1]: '1',
        configuration[2]: '2',
        configuration[3]: '3',
        configuration[4]: '4',
        configuration[5]: '5',
        configuration[6]: '6'
    }

    for inp in inputs:
        string = ""
        for c in inp:
            string += mapping[c]

        valid = [
            '012456',
            '25',
            '02346',
            '02345',
            '1235',
            '01356',
            '013456',
            '025',
            '0123456',
            '012356'
        ]

        if string not in valid:
            return False

    return True


def solve3(data):
    possibilities = generate_possibilities()

    for configuration in possibilities:
        for line in data:
            inputs = line[0]
            if is_valid(inputs, configuration):
                return configuration


def solve2(data):
    for line in data:
        inputs = line[0]
        outputs = line[1]
        possibilities = {
            "top": None,
            "top_left": None,
            "top_right": None,
            "middle": None,
            "bottom_left": None,
            "bottom_right": None,
            "bottom": None
        }

        for input in inputs:
            if len(input) == 2:
                one = input
            if len(input) == 4:
                four = input
            if len(input) == 3:
                seven = input
            if len(input) == 7:
                eight = input

        possibilities["top"] = set(seven) - set(one)

        for input in inputs:
            if len(input) == 6: #Looking for 9
                if len(set(input) - set(four) - set(possibilities["top"])) == 1:
                    possibilities["bottom"] = set(input) - set(four) - set(possibilities["top"])

        for input in inputs:
            if len(input) == 5: #Looking for 3
                if len(set(input) - set(one) - set(possibilities["top"]) - set(possibilities["bottom"])) == 1:
                    possibilities["middle"] = set(input) - set(one) - set(possibilities["top"]) - set(possibilities["bottom"])

        for input in inputs:
            if len(input) == 5: # Looking for 5
                if len(set(input) - set(one) - set(possibilities["top"]) - set(possibilities["middle"]) - set(possibilities["bottom"])) == 1:
                    possibilities["top_left"] = set(input) - set(one) - set(possibilities["top"]) - set(possibilities["middle"]) - set(possibilities["bottom"])

        possibilities["bottom_left"] = set(eight) - set(possibilities["top"]) - set(possibilities["bottom"]) - set(possibilities["middle"]) - set(one) - set(four)

        for input in inputs:
            if len(input) == 5: #Looking for 2
                if len(set(input) - set(possibilities["top"]) - set(possibilities["middle"]) - set(possibilities["bottom"]) - set(possibilities["bottom_left"])) == 1:
                    possibilities["top_right"] = set(input) - set(possibilities["top"]) - set(possibilities["middle"]) - set(possibilities["bottom"]) - set(possibilities["bottom_left"])

        possibilities["bottom_right"] = list(set(one) - set(possibilities["top_right"]))


        inv_map = {list(v)[0]: k for k, v in possibilities.items()}

        digits = ""
        for output in outputs:
            top = False
            top_left = False
            top_right = False
            middle = False
            bottom_left = False
            bottom_right = False
            bottom = False





        print(possibilities)


def main():
    lines = list(open("input.txt").read().split("\n"))
    data = []
    outputs = []

    for line in lines:
        input = line.split('|')[0].split()
        output = line.split('|')[1].split()

        outputs += output
        data.append((input, output))

    #print(outputs)
    print(solve1(outputs))
    print(solve2(data))

if __name__ == "__main__":
    main()