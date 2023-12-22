---
tag: code_problem
time_elapsed: 15
difficulty: easy
created: 2023-12-22T11:58
updated: 2023-12-22T12:29
---

# 118 - Pascals Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![[118_pascals_triangle-20231222115948639.jpg]]

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The very first thing we have to think about its how we can get the lower row. We know that each list begins and ends with a `[1]`. We also know, that to get the number below, we must add the current number with it's neighbor. Once we can get the next row from the current row, then all we need to do left is do that `numRows` amount of times to get our answer.

# Approach
<!-- Describe your approach to solving the problem. -->
I split question into another function. I created the `get_next_row(row)` function. What it does is take in a list and outputs the next row from that list. From there, I make a for loop execute `numRows` amount of times, resetting the current row to the result we get from `get_next_row(row)` and appending it to a superlist. Then we get our answer.

# Complexity
- Time complexity: $O(n^2)$ ~ this is because we iterate `numRows` amount of times, and for each we iterate the current row to get the next row.  

- Space complexity: $O(n)$ ~ this is because memory is being stored in the `rows` list. As the input increases, `rows` will linearily increase in length.

# Code
```python
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        # super list
        rows = []
        current_row = [1]
        for i in range(numRows):
            rows.append(current_row)
            current_row = get_next_row(current_row)
        return rows


def get_next_row(row):
    next_row = [1]
    for i in range(len(row) - 1):
        result = row[i] + row[i + 1]
        next_row.append(result)
    next_row.append(1)
    return next_row

```
