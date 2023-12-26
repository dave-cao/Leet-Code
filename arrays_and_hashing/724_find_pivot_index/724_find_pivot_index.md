---
tag: code_problem
time_elapsed: 11
difficulty: easy
---

# 724 - Find Pivot Index

**Notes**: Got the most optimal solution on the first try

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

 

Constraints:

    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
At first I thought this was a two-pointer question where I would need to start from the beginning and end and work my ways towards the middle. Then I realized, okay, we need to somehow store the left sum and the right sum of an index. How do we do that with only one for loop?

# Approach
<!-- Describe your approach to solving the problem. -->
What I did was initialize the left sum as 0 and the right sum as the sum of all the numbers. As we increase our index, we just need to subtract the current number to get the right sum. And to get the left sum, we continually add to our left sum. If the left sum and the right sum is the same, then we can return the index that we got. Done.

# Complexity
- Time complexity: $O(n)$ ~ because we loop through all of nums at worst case

- Space complexity: $O(1)$ ~ we only store information into left_sum and right_sum

# Code
```python
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        left_sum, right_sum = 0, sum(nums)

        for i, num in enumerate(nums):
            right_sum -= num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1

```
