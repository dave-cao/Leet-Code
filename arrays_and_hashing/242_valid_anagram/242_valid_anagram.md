---
created: 2023-12-13T17:49
updated: 2023-12-18T14:58
tag: code_problem
time_elapsed: 5
difficulty: easy
---

# 242 - Valid Anagram

**Time Elapsed**: 5 minutes
**Difficulty**: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

![[242_valid_anagram-20231214121117876.jpg]]

Input: `s = "anagram", t = "nagaram"`
Output: `true`

Example 2:

Input: `s = "rat", t = "car"`
Output: `false`

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts was to store each character into a map as a letter counter and then compare those two.

# Approach
<!-- Describe your approach to solving the problem. -->
I did exactly that, I counted the letters from each word into a letter counter map and then compared them.

# Complexity
- Time complexity: $$O(n)$$
    - the time to run will increase linearily as the input increases
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
    - the amount of memory of the map will increase as the input increases in length linearily
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # use a hashmap to store input

        s_map = self.get_char_count(s)
        t_map = self.get_char_count(t)

        return s_map == t_map

    def get_char_count(self, string: str) -> dict:

        word_map = {}
        for char in string:
            word_map[char] = word_map.get(char, 0) + 1
        return word_map

```

