iterations_count = 0


def get_possible_numbers(board: list[list[str]], row: int, col: int) -> list[str]:
    numbers = set(str(i) for i in range(1, 10))

    numbers -= set(board[row])

    numbers -= set(board[i][col] for i in range(9))

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            numbers.discard(board[start_row + i][start_col + j])

    return list(numbers)


def solve_sudoku(board: list[list[str]]) -> list[list[str]] | None:
    if not validate_sudoku(board):
        return None

    board = [row[:] for row in board]

    empty = find_empty(board)
    if not empty:
        return board

    row, col = empty

    global iterations_count
    possible_numbers = get_possible_numbers(board, row, col)

    for num in possible_numbers:
        iterations_count += 1
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
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

iterations_count = 0
result = solve_sudoku(sudoku)
print(f"Кількість ітерацій: {iterations_count}")
if result:
    print("Рішення знайдено:")
    for row in result:
        print(row)
else:
    print("Рішення не існує")
