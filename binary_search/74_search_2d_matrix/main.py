class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        left_row, right_row = 0, len(matrix) - 1

        # as long as we still have things to search
        while left_row <= right_row:

            # look for ranges
            mid_row = (right_row + left_row) // 2

            mid_start = matrix[mid_row][0]
            mid_end = matrix[mid_row][len(matrix[mid_row]) - 1]

            # if the right side (biggest) is still smaller
            # then our target, then discard all lower rows
            if mid_end < target:
                left_row = mid_row + 1
            # if the left side (smallest) is still bigger
            # then our target, then discard all bigger row
            elif mid_start > target:
                right_row = mid_row - 1
            else:
                left, right = 0, len(matrix[mid_row]) - 1
                while left <= right:
                    mid = (right + left) // 2
                    if matrix[mid_row][mid] < target:
                        left = mid + 1
                    elif matrix[mid_row][mid] > target:
                        right = mid - 1
                    else:
                        return True

                return False
        return False


def main():
    solution = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 20
    print(solution.searchMatrix(matrix, target))


if __name__ == "__main__":
    main()

# step 1
# - find if it is within ranges
# - search through every row

# step 2
# find if it is within row
# - search every element in row
