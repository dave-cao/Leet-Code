---
created: 2023-12-17T10:51
updated: 2023-12-18T14:58
tag: code_problem
time_elapsed: 5
difficulty: medium
---

# 167 - Two Sum II - Input Array is Sorted

**Time Elapsed**: 5 minutes
**Difficulty**: Medium
**Thoughts**: Simple question, made me understand two pointers a bit more


Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

 

Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This problem intuitively is very similar to the two sum number one question. My first thoughts was to use a map to just do the same thing as two_sum. However, this question I wanted to complete using two-pointers.

# Approach
<!-- Describe your approach to solving the problem. -->
Since I know that the input array will already be sorted, we can have two pointers. One at the end and one at the beginning of the array. From there, we compare if the addition between the two pointers is our target. If the sum is lower then the target, the only way to increase the number is to increment our start pointer by one. Conversely, if the sum is less than, then we decrease the number by decreasing the increment of the end pointer. Eventually we will find the sum that matches our target.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python

class Solution:
    # two-pointer solution
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            # this method works because it is already sorted
            elif sum < target:
                # if the sum if less then target, increase the increment (this strictly
                # increases the number since it is sorted)
                left += 1
            else:
                # strictly decreases the number
                right -= 1
```

