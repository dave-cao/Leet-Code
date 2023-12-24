---
tag: code_problem
time_elapsed: 23
difficulty: easy
process: completed
created: 2023-12-24T12:27
updated: 2023-12-24T13:02
---

# 205 - Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

 

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first intuition with this problem is that each letter must have the same amount of **unique** letters to each other. Then, we have to take into account that each letter must also be in the same order.

# Approach
<!-- Describe your approach to solving the problem. -->
I used a map approach to solve this problem. If a letter wasn't mapped yet, I would map it to the corresponding letter in $t$ (only if that letter hasn't been used yet). If at all, we grab the mapped char and it doesn't correspond with $t$ then it is not isomorphic.

# Complexity
- Time complexity: $O(n)$ ~ we iterate through $s$ once.

- Space complexity: $O(n)$ ~ map increases linearly if all values of $s$ and $t$ are unique

# Code
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # both strings need to be of same length
        if len(s) != len(t):
            return False

        map = {}
        for i, char in enumerate(s):

            # if the char hasn't been mapped yet, map it
            if not map.get(char):

                # so long as the value to be mapped is not already used
                if t[i] not in map.values():
                    map[char] = t[i]

            # return false if the mapped char isn't correct
            if map.get(char, "") != t[i]:
                return False
        return True


```
