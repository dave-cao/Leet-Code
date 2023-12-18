from pprint import pprint


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


def main():
    sol = Solution()

    board_one = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",

                                                                                                                                                                                                              "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                          "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    sol.isValidSudoku(board_one)


if __name__ == "__main__":
    main()
