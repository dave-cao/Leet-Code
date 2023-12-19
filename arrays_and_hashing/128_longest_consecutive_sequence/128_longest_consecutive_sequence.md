---
tag: code_problem
time_elapsed: 39
difficulty: medium
created: 2023-12-15T08:10
updated: 2023-12-18T14:58
---

# 128 - Longest Consecutive Sequence

**Time Elapsed**: 39 minutes
**Difficulty**: medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109

---

# Notes
- I had a plan to tackle this using two_sum, but I couldn't really figure it out
- I would have gotten the difference, (plus, minus) and put it in a map, and then would have grabbed the numbers going down. Not sure if that was the right way to do it.

- my bs solution is sorting it (I know, we probably should use the sort method)
- then counting streaks from there.
- then we have to count for duplicates, so I have another function that filters for duplicates

## Looking at the Solution
So looking at the solution, what we have to do is look for the starting values of each sequence. The starting values would be numbers don't have a left neighbor; as in, they don't have a number that is 1 less than it in the list. If we can get that, we can make another loop (while loop), to check for right neighbors. 

This solution would have been hard to think of because it uses a loop within a loop which intuitively tells me its not $O(n)$ complexity.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts while looking at this was that we might have to use the same logic as two_sum and get the difference and store it in a map. However, that proved to be too difficult for me, so I decided to just use the Sorted method and go from there.

# Approach
<!-- Describe your approach to solving the problem. -->
I first turned the numbers into a set to get rid of all duplicates (then back to a list), then I sorted it. From there, I just counted consecutive numbers, and if another streak is longer than another then we replace the longest streak counter.

# Complexity
- Time complexity: $O(n)$
    - it's not really O(n) if we use the sorted method I don't think

- Space complexity: $O(n)$

# Code
```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)

        if not nums:
            return 0

        streak = 1
        current_streak = 1
        for i in range(len(nums) - 1):
            current = nums[i]
            next = nums[i + 1]

            if next == current + 1:
                current_streak += 1
            if next != current + 1 or (i == (len(nums) - 2)):
                if current_streak != 1:
                    if current_streak > streak:
                        streak = current_streak
                current_streak = 1
        return streak

```
