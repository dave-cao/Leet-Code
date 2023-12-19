---
created: 2023-12-14T12:10
updated: 2023-12-18T14:58
tag: code_problem
time_elapsed: 34
difficulty: medium
---

# 36 - Valid Sudoku


Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
When I first looked at this question I immediately thought of a matrix type question. We just had to get a list of each row, each column and each square, and then see if it's valid or not.

# Approach
<!-- Describe your approach to solving the problem. -->
I created a separate function to see if a list of numbers is a valid list of numbers. From there, I used a separate function to check each row, another function that turned columns into rows (and then checked) and another one that turned each square into rows (and then checked that). From there, I checked each function, and if all of them are true, then it is a valid sudoku.

# Complexity
- Time complexity: $O(n^2)$
    - requires a loop within a loop


- Space complexity: $O(n)$
    - I'm not really sure to be honest


# Code
```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # check if a list is a valid list
        check_states = has_valid_rows(board) and has_valid_columns(
            board) and has_valid_square(board)
        return check_states


def has_valid_square(board):

    map = {}
    for row_i in range(len(board)):
        box_row = row_i // 3

        for col_i in range(len(board[0])):
            box_col = col_i // 3

            # store each square into its individual map
            box_coord = str((box_row, box_col))
            if map.get(box_coord) is None:
                map[box_coord] = [board[row_i][col_i]]
            else:
                map.get(box_coord).append(board[row_i][col_i])

    for line in map.values():
        if not is_valid_line(line):
            return False
    return True


def has_valid_columns(board):
    for col_i in range(len(board[0])):
        column = [board[row_i][col_i] for row_i in range(len(board))]
        if not is_valid_line(column):
            return False
    return True


def has_valid_rows(board):
    for row in board:
        # if any row is not valid, then return False
        if not is_valid_line(row):
            return False
    return True


def is_valid_line(nums):
    map = {}

    # for every number
    for num in nums:
        # check if the number is a valid number
        if num.isnumeric():
            # add the count to map
            map[num] = map.get(num, 0) + 1
            # if theres more then 1, then return False
            if map.get(num) > 1:
                return False
    return True

```
