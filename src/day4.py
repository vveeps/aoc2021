from getlines import lines

lines = [i for i in lines if i]
drawn_numbers = [int(i) for i in lines.pop(0).split(",")]


class BingoBoard:
    def __init__(self, rows: list[list[str]]):
        self.rows = rows
        self.all = set(num for row in self.rows for num in row)

        self.hits: list[tuple[int, int]] = []

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.rows == other.rows

    def __iter__(self):
        return (row for row in self.rows)


def p1():
    boards = [
        BingoBoard([[int(i) for i in row] for row in [row.split() for row in board]])
        for board in [lines[i:i+5] for i in range(0, len(lines), 5)]
    ]

    done = False
    for num in drawn_numbers:
        for board in boards:
            if num in board.all:
                for y_idx, y in enumerate(board.rows):
                    if num in y:
                        x_idx = y.index(num)
                        board.hits.append((x_idx, y_idx))

                board.all.remove(num)

            if len(board.hits) >= 5:
                x_hits = [i[0] for i in board.hits]
                y_hits = [i[1] for i in board.hits]

                if any(x_hits.count(num) >= 5 for num in set(x_hits)) \
                   or any(y_hits.count(num) >= 5 for num in set(y_hits)):
                    done = True
                    break

        if done:
            break

    unmarked_sum = sum(board.all)
    return unmarked_sum * num


def p2():
    boards = [
        BingoBoard([[int(i) for i in row] for row in [row.split() for row in board]])
        for board in [lines[i:i+5] for i in range(0, len(lines), 5)]
    ]

    done = False
    for num in drawn_numbers:
        for board in boards:
            tmp = boards[:]
            if num in board.all:
                for y_idx, y in enumerate(board.rows):
                    if num in y:
                        x_idx = y.index(num)
                        board.hits.append((x_idx, y_idx))

                board.all.remove(num)

            if len(board.hits) >= 5:
                x_hits = [i[0] for i in board.hits]
                y_hits = [i[1] for i in board.hits]

                if any(x_hits.count(num) >= 5 for num in set(x_hits)) \
                   or any(y_hits.count(num) >= 5 for num in set(y_hits)):
                    if len(boards) == 1:
                        done = True
                        break
                    tmp.remove(board)

            boards = tmp

        if done:
            break

    unmarked_sum = sum(board.all)
    return unmarked_sum * num


print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")
