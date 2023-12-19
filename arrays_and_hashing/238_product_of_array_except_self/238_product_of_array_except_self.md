---
tag: code_problem
time_elapsed: 46
difficulty: medium
completion_method: walkthrough
created: 2023-12-14T00:17
updated: 2023-12-18T14:58
---
# 238 - Product of Array Except Self

**Time Elapsed**: 46 min ~ didn't understand how to do the question, watched walkthrough
**Difficulty**: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts for this question was to use slicing and just slice the first half, then the second half, and then add them together and get the product. However, we won't be able to get a time complexity of $O(n)$ this way!

# Approach
<!-- Describe your approach to solving the problem. -->
Watching the video from NeetCode, we basically have to get a prefix multiplication value and a postfix multiplication value. If we multiply the prefix and the postfix, before and after the number that we want, then we get our answer.

You have to use two loops. The first loop, you put the prefixes into a list. Remember that the prefixes are before the `i`. Since the first number never has a prefix (since it's first), it will have a starting value of 1. 

On the second loop, you work backwards and multiply the already stored prefix by the postfix that you get. Ultimately you get your answer.

![[238_product_of_array_except_self-20231214011622361.jpg]]

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = 1
        postfix = 1
        result = [0] * n

        # store the prefix first
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # multiply the now stored prefix by the postfix
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

```
