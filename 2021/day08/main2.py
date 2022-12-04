with open("input.txt") as file:
    signals = [["".join(sorted(digit)) for digit in row] for row in (row.replace(" | ", " ").split() for row in file)]

number_of_1478 = sum(len([digit for digit in row[-4:] if len(digit) not in range(5, 7)]) for row in signals)

sum_of_outputs = 0
for row in signals:
    segments = {}
    for digit in row[:10]:
        if len(digit) == 2:
            segments[1] = digit
        elif len(digit) == 3:
            segments[7] = digit
        elif len(digit) == 4:
            segments[4] = digit
        elif len(digit) == 7:
            segments[8] = digit
    for digit in row[:10]:
        if len(digit) == 5:
            if all(ch in digit for ch in segments[1]):
                segments[3] = digit
            elif len([ch for ch in segments[4] if ch in digit]) == 3:
                segments[5] = digit
            else:
                segments[2] = digit
        elif len(digit) == 6:
            if not all(ch in digit for ch in segments[1]):
                segments[6] = digit
            elif not all(ch in digit for ch in segments[4]):
                segments[0] = digit
            else:
                segments[9] = digit

    print(segments)
    segments = {v: str(k) for k, v in segments.items()}
    print(segments)
    sum_of_outputs += int("".join(segments[digit] for digit in row[-4:]))

print(number_of_1478)
print(sum_of_outputs)