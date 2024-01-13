---
tag: code_problem
diffculty: hard
time_elapsed: 60
process: tutorial
created: 2024-01-12T12:19
updated: 2024-01-12T21:18
---

# 76 - Minimum Window Substring

**Note**: I was able to get the brute force answer but it exceeded time limit
*Notes*: No way I would have been able to figure that out by myself

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

---

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # initialize counter for t
        t_counter = {}
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1

        # we need the characters we have in t
        have, need = 0, len(t_counter)
        res = (-1, -1)
        min_len = float("inf")

        # intialize a window counter
        window_counter = {}
        left = 0
        for right in range(len(s)):
            char = s[right]
            window_counter[char] = window_counter.get(char, 0) + 1

            if char in t_counter and window_counter[char] == t_counter[char]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = (left, right)

                # pop from the left of our window
                window_counter[s[left]] -= 1
                if s[left] in t_counter and window_counter[s[left]] < t_counter[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left: right + 1] if min_len != float("inf") else ""

    def minWindow_time_exceeded(self, s: str, t: str) -> str:

        # if s is less then t, then there is no way
        # for t to be a substring of s
        if len(s) < len(t):
            return ""
        # if they are the same string, then return s
        elif s == t:
            return s

        chars = [*t]

        left, right = 0, 0
        min_window = float("inf")
        min_coords = None
        while right < len(s):

            # if we get a match, remove it from chars
            if s[right] in chars:
                chars.remove(s[right])

            # If we found all the characters
            if not chars:
                window_len = right - left + 1
                if window_len < min_window:
                    min_window = window_len
                    min_coords = (right, left)

                # reset the chars
                chars = [*t]

                # update the left pointer by one
                left += 1

                # update the left pointer until we find a match
                while left < len(s) and s[left] not in chars:
                    # if the left pointer reaches the right pointer
                    # then shift the right pointer back
                    if left == right:
                        right = left - 1
                        break

                    left += 1
                right = left - 1

            right += 1

        if min_coords:
            right, left = min_coords
            return (s[left: right+1])
        else:
            return ""
```
