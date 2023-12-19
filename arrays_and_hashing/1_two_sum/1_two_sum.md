---
created: 2023-12-13T18:04
updated: 2023-12-18T14:58
tag: code_problem
time_elapsed: 10
difficulty: easy
---

# 1 - Two Sum

**Time Elapsed**: 10 min 
**Difficulty**: Easy

*Note*: couldn't figure out how to do it not with 0(n^2) complexity without looking at a solution.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

--- 

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts were to do the brute force method and making two for loops. However, after looking at a solution, I saw someone use a dictionary to store the **difference** of the target number with the current number.
# Approach
<!-- Describe your approach to solving the problem. -->
Basically what you do is loop through each number, and store the difference into a map. For example, if you have the number `4` and a target of `9`, then the next number you would be looking for is `5` or `9 - 4 = 5`. Thus, if you encounter a 5, then you just have to grab the index you stored and return it with the difference you just encountered!
- surprisingly, the brute force method that I did gave a lower space complexity then this solution.

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(n)$

# Code
```python
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        word_map = {}
        # basically we are searching for the difference
        # of the numbers that we found already
        for i, num in enumerate(nums):
            if num in word_map:
                return [word_map[num], i]
            else:

                # target - num is key here
                # eg: if our target is 9 and our first element is 1,
                # then if we ever encounter an 8, then 1 + 8 = 9
                # omg this is so genius
                word_map[target - num] = i
 
 
```

