---
tag: code_problem
difficulty: easy
time_elapsed: 5
created: 2024-01-20T13:37
updated: 2024-01-20T13:37
---

# [704. Binary Search](https://leetcode.com/problems/binary-search/)

## Quick Notes

- Binary search is a search algorithm that finds the position of a target value within a sorted array.
- two pointers and find mid point
- loop ends if left <= right

---

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Pretty simple binary search implementation using while loops.

# Approach
<!-- Describe your approach to solving the problem. -->
Set two pointers, right and left. Then get the mid point by right + left // 2. Keep the loop going as long as left <= right. Find your mid point.

# Complexity
- Time complexity: $O(logn)$


- Space complexity: $O(1)$

# Code
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            # 1 + ((right - left) // 2)
            mid = (right + left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
```
