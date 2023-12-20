---
tag: code_problem
time_elapsed: 13
difficulty: easy
created: 2023-12-20T11:29
updated: 2023-12-20T11:29
---

# 392 - Is Subsequence

**Notes**: Wasn't hard. Took me a bit of time to actually think about the solution to the problem though.

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

 

Constraints:

    0 <= s.length <= 100
    0 <= t.length <= 104
    s and t consist only of lowercase English letters.

 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts on completing this question was slicing the string into sizes of length `s` but that clearly doesn't work. I think the key here is to figure out that we only need to find the characters in a row. As in it doesn't matter if we have two of the same characters in a row. Therefore, once we find a match to one character, we can move on and look for the next character without worrying about the previous character.
# Approach
<!-- Describe your approach to solving the problem. -->
I used a while loop and two indices. One of the index tracked the substring and the other tracked the superstring. We start by seeing if the first character of the substring is the same as any character in the superstring. If we find a match, then we can look for the next character. All the while, we are updating our superstring index. 

# Complexity
- Time complexity: $O(len(t))$ ~ traverses the string `t` once 
- Space complexity: $O(1)$ ~ constant space is used

# Code
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_index = 0
        t_index = 0

        # stop either when we found a substring, or if we fully explored our string
        while s_index < len(s) and t_index < len(t):

            s_char = s[s_index]
            t_char = t[t_index]

            # if we have a match, look for next character
            if s_char == t_char:
                s_index += 1

            # continuously update t (we want subsequences)
            t_index += 1

        # returns true if all chars have s have been traversed
        return s_index == len(s)

```
