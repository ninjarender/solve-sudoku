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

def is_valid_unit(unit):
    nums = [x for x in unit if x != "."]
    return len(nums) == len(set(nums))
