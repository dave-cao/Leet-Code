---
tag: code_problem
time_elapsed: 5
difficulty: easy
created: 2023-12-19T12:42
updated: 2023-12-19T12:55
---

# 1929 - Concatenation of Array

**Note**: pretty simple question where you multiply the output an array.

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

 

Constraints:

    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts was to just multiply the list by 2 (because python lets you do that). But, I figured it was best to use arrays and indexing.

# Approach
<!-- Describe your approach to solving the problem. -->
I know that we want to return the same list but it added to itself. Therefore, we can save a little space by starting with itself. Then, we just loop through itself and add itself to itself!

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```python
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

```
