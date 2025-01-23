def solve_sudoku(board: list[list[str]]) -> list[list[str]] | None:
    if not validate_sudoku(board):
        return None

    board = [row[:] for row in board]

    empty = find_empty(board)
    if not empty:
        return board

    row, col = empty

    for num in map(str, range(1, 10)):
        if is_safe(board, row, col, num):
            board[row][col] = num

            result = solve_sudoku(board)
            if result is not None:
                return result

            board[row][col] = "."

    return None

def validate_sudoku(board: list[list[str]]) -> bool:
    for row in board:
        if not is_valid_unit(row):
            return False

    for col in zip(*board):
        if not is_valid_unit(col):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(board[box_row + i][box_col + j])
            if not is_valid_unit(box):
                return False

    return True

def is_valid_unit(unit: list[str]) -> bool:
    nums = [x for x in unit if x != "."]
    return len(nums) == len(set(nums))

def find_empty(board: list[list[str]]) -> tuple[int, int] | None:
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return (i, j)
    return None

def is_safe(board: list[list[str]], row: int, col: int, num: str) -> bool:
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

sudoku = [
    ["3", ".", "6", "5", ".", "8", "4", ".", "."],
    ["5", "2", ".", ".", ".", ".", ".", ".", "."],
    [".", "8", "7", ".", ".", ".", ".", "3", "1"],
    [".", ".", "3", ".", "1", ".", ".", "8", "."],
    ["9", ".", ".", "8", "6", "3", ".", ".", "5"],
    [".", "5", ".", ".", "9", ".", "6", ".", "."],
    ["1", "3", ".", ".", ".", ".", "2", "5", "."],
    [".", ".", ".", ".", ".", ".", ".", "7", "4"],
    [".", ".", "5", "2", ".", "6", "3", ".", "."],
]

result = solve_sudoku(sudoku)
if result:
    print("Рішення знайдено:")
    for row in result:
        print(row)
else:
    print("Рішення не існує")
