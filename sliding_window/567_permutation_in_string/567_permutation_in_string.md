---
tag: code_problem
difficulty: medium
time_elapsed: 9
created: 2024-01-12T11:51
updated: 2024-01-12T11:51
---

# 567 - Permutation in String

*Type*: Sliding Window
**Note**: his explanation was a lot different then what I did

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We know that this is a sliding window problem. By intuition, its a fixed sliding window problem, where we check every substring. The tricky part is to find the permutation.

# Approach
<!-- Describe your approach to solving the problem. -->
To find the permutation, I just turned the strings into lists, and sorted them so that it would be the same configuration every time.

# Complexity
- Time complexity: $O(n)$ ~ one while loop, might be a little bit more then this

- Space complexity:  $O(n)$ ~ storing two lists

# Code
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1, s2 = [*s1], [*s2]
        s1.sort()

        left, right = 0, len(s1) - 1
        while right < len(s2):
            window = (s2[left:right + 1])
            window.sort()

            if s1 == window:
                return True

            left += 1
            right += 1

        return False

```

