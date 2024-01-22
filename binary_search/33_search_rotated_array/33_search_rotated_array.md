---
tag: code_problem
difficulty: medium
time_elapsed: 32
---

# [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Quick Notes

- binary search
- find the quadrant of the current mid and the target
- if the target is in the same quadrant as the current mid, do regular binary search
- if the target is in the opposite quadrant as the current mid, move to the opposite quadrant
- time complexity: $O(log(n))$
- space complexity: $O(1)$

---

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Very similar to the previous rotation question we had before. But this time instead of getting the minimum, we are finding a target.

# Approach
<!-- Describe your approach to solving the problem. -->
We first have to figure out if our current mid is in the left or right quadrant. If our current is in the left quadrant and our target is in the right qudrant, move to the right. Otherwise, do regular binary search. Note that if our current is equal to the first num, it is automatically gonna be in the left quadrant. On the other hand, if the current is in the right qudrant and the target is in the left qudrant, then move to the right, otherwise, do regular binary search.

# Complexity
- Time complexity: $O(log(n))$

- Space complexity: $O(1)$

# Code
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        first_num = nums[0]
        while left <= right:
            mid = (right + left) // 2
            mid_num = nums[mid]
            right_quad = target < first_num

            # current quadrant is left quad
            if mid_num >= first_num:

                # if the target is in the right quad
                # and we are in the left quad, then go to the right
                if right_quad:
                    left = mid + 1
                # if the target is in the left quad
                # and we are in the left quad, then do regular binary search
                else:
                    # then do regular binary search
                    if mid_num < target:
                        left = mid + 1
                    elif mid_num > target:
                        right = mid - 1
                    else:
                        return mid

            # current quadrant is right quad
            elif mid_num < first_num:

                # if the target is in the right quad
                # and we are in the right quad
                if right_quad:
                    # then do regular binary search
                    if mid_num < target:
                        left = mid + 1
                    elif mid_num > target:
                        right = mid - 1
                    else:
                        return mid
                else:
                    # otherwise, go to the left quad
                    right = mid - 1
        return -1


```
