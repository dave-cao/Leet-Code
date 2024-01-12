---
tag: code_problem
difficulty: medium
time_elapsed: 50
process: tutorial
created: 2024-01-11T20:45
updated: 2024-01-11T22:12
---

# 424 - Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I'll be honest I had no clue how to start this question, I had to use a tutorial.

# Approach
<!-- Describe your approach to solving the problem. -->
You have to initialize a map that counts your characters. And then make a sliding window. The key here is that the largest window we can have is when the window size - most frequent letter count is less than or equal to k! 

# Complexity
- Time complexity: $O(n)$


- Space complexity: $O(n)$


# Code
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # initalize a map that counts letters
        count = {}

        left = 0
        max_count = 0

        # go through every letter
        for r in range(len(s)):
            # add each letter to our map
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            max_count = max(max_count, r - left + 1)

        return max_count

```
