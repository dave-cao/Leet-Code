---
tag: code_problem
difficulty: medium
time_elapsed: 30
---

# 74. Search a 2D Matrix
<https://leetcode.com/problems/search-a-2d-matrix/>

## Quick Notes

- Binary search within a binary search
- Time complexity: $O(log(n * m))$
- Space complexity: $O(1)$
- If smallest number of mid row is bigger than target, then discard all rows above it
- If biggest number of mid row is smaller than target, then discard all rows below it

---

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Simple binary within a binary problem. If you know how to do binary search, then you will know how to do this problem.

# Approach
<!-- Describe your approach to solving the problem. -->
First I had to find smallest and biggest numbers of the mid row we are looking at. And check if the smallest number is bigger than our target or if the biggest number is smaller than our target. If the biggest number is smaller than our target, we can discard this range and all rows beneath it. If the smallest number is bigger than the target, then we can discard this range and all rows above it.

# Complexity
- Time complexity: $O(log(n * m))$

- Space complexity: $O(1)$

# Code
```python
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

```
