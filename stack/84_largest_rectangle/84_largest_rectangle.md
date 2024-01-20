---
tag: code_problem
difficulty: hard
time_elapsed: 120
process: tutorial
created: 2024-01-20T12:03
updated: 2024-01-20T13:30
---

# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Quick Notes

- [Monotonically increasing stack](https://www.youtube.com/watch?v=VNbkzsnllsU)
- When getting the width, set the current index to the most recent pop's index

---

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This is a monotonically increasing stack. We have to figure out that the largest rectangle of the current is when the bar next to is is smaller than it. If it is bigger, then you can continue to extend the previous bar.

# Approach
<!-- Describe your approach to solving the problem. -->
Create a stack. If the current is greater than what is less than what is in the stack, then pop the stack and do your calculation on it. Continue until it is less than, then you can just append.


# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(n)$

# Code
```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []  # stores (index, height)
        maxArea = 0

        # first run
        for i, height in enumerate(heights):
            # counts how many times we popped
            start = i
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                width = i - index
                area = h * width

                maxArea = max(maxArea, area)

                # set the start index back to the most recent pop's index
                start = index

            stack.append((start, height))

        if stack:
            for i, height in stack:
                width = len(heights) - i
                area = width * height
                maxArea = max(maxArea, area)
        return maxArea

```
