# Simple Validator for a Sudoku Board

Suppose you are tasked with designing a simple validator for a partially filled 9x9 Sudoku board. Your primary job is to check if the current filled entries of the board follow the Sudoku rules or not. Your task is to return a boolean, stating whether the board is valid or not.

## Validation Rules

The rules for an entry to be valid are as follows:

1. **Row Validation**: Each row of the board can contain digits 1-9, without any repetition.
2. **Column Validation**: Each column of the board can contain digits 1-9, without any repetition.
3. **Sub-box Validation**: Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition. 

   **Note**: Each 3x3 sub-box contains 9 cells, and there are 9 sub-boxes, and each cell belongs to only one sub-box. There is only one way to place them. If you are still not sure if you get it right, read the Sudoku rules.

## Important Considerations

It's important to keep in mind that:

- The Sudoku board could be partially filled, and it could be valid but not necessarily solvable.
- You are only expected to verify the existing filled entries. Unfilled entries are not part of the validation process.

## Task

Your function will receive a 9x9 2D array (matrix) as its input, representing the Sudoku board. The empty cells will be represented by the `.` character. You need to return `True` if the board is valid according to the Sudoku rules, and `False` otherwise.

## Example

```python
>>> validate_sudoku([
        ['3', '.', '6', '5', '.', '8', '4', '.', '.'], 
        ['5', '2', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '8', '7', '.', '.', '.', '.', '3', '1'], 
        ['.', '.', '3', '.', '1', '.', '.', '8', '.'], 
        ['9', '.', '.', '8', '6', '3', '.', '.', '5'], 
        ['.', '5', '.', '.', '9', '.', '6', '.', '.'], 
        ['1', '3', '.', '.', '.', '.', '2', '5', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '7', '4'], 
        ['.', '.', '5', '2', '.', '6', '3', '.', '.'] 
    ])
True
```