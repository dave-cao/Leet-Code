---
tag: code_problem
time_elapsed: 9
difficulty: easy
created: 2023-12-25T00:21
updated: 2023-12-25T00:21
---

# 169 - Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109

 
Follow-up: Could you solve the problem in linear time and in O(1) space?

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts were that we needed to count the number of occurrences of each number. Then get the element that occurs more then floor(n / 2) times. We first need to get the number that occurs the most. So first, we should count the number of occurrences of a number, and then get the max number that was counted. Done.

# Approach
<!-- Describe your approach to solving the problem. -->
Make a map that counts the number of times a number occurs. Then another for loop that gets the key that has the max occurrences. Then return that key.


# Complexity
- Time complexity: $O(n)$ ~ we must loop through nums once

- Space complexity: $O(n)$ ~ we use a map to store the occurrences of a number

# Code
```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # create a counter, that counts
        # occurences of number
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        # get the map element that occurred
        majority_count = 0
        majority = 0
        for num, count in map.items():
            if count > majority_count:
                majority_count = count
                majority = num

        return majority

```
