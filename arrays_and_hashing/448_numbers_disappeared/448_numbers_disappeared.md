---
tag: code_problem
time_elapsed: 16
difficulty: easy
created: 2023-12-30T13:56
updated: 2023-12-30T17:34
process: tutorial
---

# 448 - Find All Numbers Disappeared in An Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Wasn't too sure how to approach this. Got a brute force solution at first but it exceeded the time limit. After watching the solution I have a better understanding of how to answer this question.

# Approach
<!-- Describe your approach to solving the problem. -->
Basically what you have to do is mark a number as negative with it's own array if it exists within its own array. We have a mapping of `i + 1` which is the same as what we want to find. Then we get any `i + 1` that isn't negative.  


# Complexity
- Time complexity: $O(n)$ ~ we are looping through once to mark each number, and then we are looping again to get the positive numbers only


- Space complexity: $O(1)$ ~ because we are rearranging the input array itself.

# Code
```python
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # mark each number in its own array as negative if it exists
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        # get only positives
        result = []
        for i, num in enumerate(nums):
            if num >= 0:
                result.append(i + 1)
        return result

```
