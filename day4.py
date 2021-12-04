from shared import get_lines_from_file


class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False

    def mark_cell(self):
        self.marked = True


class Board:
    def __init__(self, board):
        self.board = self.initialize_board(board)

    def initialize_board(self, board):
        initialized_board = []
        for row in board:
            initialized_row = []
            for number in row:
                initialized_row.append(Cell(number))
            initialized_board.append(initialized_row)
        return initialized_board

    def mark_number(self, number):
        for row in self.board:
            for cell in row:
                if cell.value == number:
                    cell.marked = True

    def is_completed(self):
        return self._has_completed_row() or self._has_completed_column()

    def calculate_score(self, called_number):
        sum_of_unmarked = 0
        for row in self.board:
            for cell in row:
                if not cell.marked:
                    sum_of_unmarked += cell.value

        return sum_of_unmarked * called_number

    def __str__(self):
        result = []
        for row in self.board:
            row_to_print = []
            for cell in row:
                row_to_print.append(str(cell.value))
                if cell.marked:
                    row_to_print.append("(+) ")
                else:
                    row_to_print.append("(-) ")
            row_to_print.append("\n")
            result.append("".join(row_to_print))
        return "".join(result)

    def _has_completed_row(self):
        for row in self.board:
            completed = True
            for cell in row:
                if not cell.marked:
                    completed = False
                    break
            if completed:
                return True
        return False

    def _has_completed_column(self):
        num_of_columns = len(self.board[0])

        for col in range(num_of_columns):
            completed = True
            for row in self.board:
                cell = row[col]
                if not cell.marked:
                    completed = False
                    break
            if completed:
                return True
        return False


def calculate_winning_score(moves, boards):
    initialized_boards = []
    for board in boards:
        initialized_boards.append(Board(board))

    for move in moves:
        update_boards_with_move(move, initialized_boards)
        if is_any_board_completed(initialized_boards):
            completed_board = get_completed_board(initialized_boards)
            return completed_board.calculate_score(move)


def update_boards_with_move(move, boards):
    for board in boards:
        board.mark_number(move)


def is_any_board_completed(boards):
    for board in boards:
        if board.is_completed():
            return True
    return False


def get_completed_board(boards):
    for board in boards:
        if board.is_completed():
            return board


def get_moves_from_line(line):
    moves_string = line.split(",")
    return [int(move) for move in moves_string]


def get_boards_from_lines(lines):
    boards = []
    current_board = []

    for i in range(len(lines)):
        line = lines[i]
        if not line.strip():
            boards.append(current_board)
            current_board = []
        else:
            row_string = line.split()
            row = [int(number) for number in row_string]
            current_board.append(row)

    return boards


def calculate_losing_score(moves, boards):
    initialized_boards = []
    for board in boards:
        initialized_boards.append(Board(board))

    for move in moves:
        update_boards_with_move(move, initialized_boards)
        new_initialized_boards = remove_completed_boards(initialized_boards)
        if len(initialized_boards) == 1 and len(new_initialized_boards) == 0:
            return initialized_boards[0].calculate_score(move)
        initialized_boards = new_initialized_boards


def remove_completed_boards(boards):
    result = []
    for board in boards:
        if not board.is_completed():
            result.append(board)
    return result


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day4.txt")
    assert len(lines) > 3
    moves = get_moves_from_line(lines[0])
    boards = get_boards_from_lines(lines[2:])

    print(calculate_winning_score(moves, boards))
    print(calculate_losing_score(moves, boards))
