from textwrap import wrap


def to_decimal(number):
    return int(number, 2)


def get_headers(binary):
    return to_decimal(binary[0:3]), to_decimal(binary[3:6])


def convert(packet):
    return "{0:8b}".format(int(str(1) + packet, 16))[1:]


def read_packets(binary, length):
    return wrap(binary, 11)[0:length]


def parse_operator(packet):
    mode = int(packet[0])

    if mode == 0:
        len_sub_packets = to_decimal(packet[1:16])
        literals = parse_literal(packet[16:16 + len_sub_packets])
    if mode == 1:
        num_sub_packets = to_decimal(packet[1:12])
        packets = read_packets(packet[12:], num_sub_packets)
        print(packets)




def parse_literal(binary):
    pad = len((binary)) % 5
    numbers = binary[:len(binary) - pad]

    split_numbers = [x[1:] for x in wrap(numbers, 5)]

    sum = to_decimal(''.join(split_numbers))

    return sum


def main():
    packet = open("input4.txt").read().rstrip()

    binary = convert(packet)

    version, type = get_headers(binary)

    match type:
        case 4:
            numbers = parse_literal(binary[6:])
        case _:
            something = parse_operator(binary[6:])

    print(version, type)


if __name__ == "__main__":
    main()