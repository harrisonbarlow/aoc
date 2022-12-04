
class Board():
    def __init__(self, board):
        self.board = board

    def __str__(self):
        output = ""
        for row in self.board:
            output += str(row)
            output += '\n'
        return output

    def is_solved(self):
        if self.rows() or self.columns():
            return True
        else:
            return False

    def rows(self):
        for row in self.board:
            status = []
            for column in row:
                status.append(column[1])
            if all(status):
                return True
        return False

    def columns(self):
        for column in range(len(self.board[0])):
            status = []
            for row in self.board:
                status.append(row[column][1])

            if all(status):
                return True
        return False

    def mark(self, number):
        for row in self.board:
            for column in row:
                if column[0] == number:
                    column[1] = True

    def score(self):
        total = 0
        for row in self.board:
            for column in row:
                if column[1] is False:
                    total += column[0]

        return total

def solve1(boards, drawn):
    found = False
    for number in drawn:
        for board in boards:
            board.mark(number)
            if board.is_solved():
                print(board)
                print(board.score() * number)
                found = True
            if found:
               break
        if found:
           break
            

def solve2(boards, drawn):
    for number in drawn:
        for board in list(boards):
            board.mark(number)
            if board.is_solved():
                if len(boards) == 1:
                    print(board)
                    print(board.score() * number)
                boards.remove(board)

def main():
    drawn = []
    parsed = []
    boards = []

    for i, line in enumerate(open("input.txt")):
        trimmed = line.rstrip()
        if i == 0:
            drawn = trimmed.split(',')
            drawn = [int(draw) for draw in drawn]
            continue

        if i == 1:
            continue

        if line == "\n":
            boards.append(Board(parsed))
            parsed = []
            continue

        line = []
        for number in trimmed.split():
            line.append([int(number), False])

        parsed.append(line)
        line = []

    solve1(boards, drawn)
    solve2(boards, drawn)

if __name__ == "__main__":
    main()