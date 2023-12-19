---
tag: code_problem
time_elapsed: 17
difficulty: medium
created: 2023-12-17T23:15
updated: 2023-12-18T14:58
---
# 11 - Container With Most Water

- **Time Elapsed**: 17 minutes
- **Difficulty**: medium
- *notes*: Pretty straight forward once you write it out

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts on completing this problem was juts to brute force it. All we need to do is make a nested for loop getting each possible pair and their x and y dimensions. From there, I simplified it down to a two-pointer question.

# Approach
<!-- Describe your approach to solving the problem. -->
I used a two pointer where we have a left and a right pointer. The left pointer is at the beginning of the array and the right pointer is at the end. We first get the `x` and `y` from this beginning pair. Next is the tricky part. We know that this right now is the largest `x` possible. We can only decrease `x` from here (increment the left pointer or decrement the right pointer). That means, if we keep the smallest pointer, any changes in `x` will strictly be less than what we have right now! Therefore, we must change the smaller pointer! One we do that, then we check the `x` and `y` again, and redo the process until we get an `x` of 0.

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(n)$

# Code
```python
class Solution:
    def maxArea(self, height: list[int]) -> int:

        # first make right and left pointers
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            x = right - left
            y = min(height[left], height[right])
            water = x * y

            if water > max_water:
                max_water = water

            if y == height[left]:
                left += 1
            else:
                right -= 1

        return max_water

```


