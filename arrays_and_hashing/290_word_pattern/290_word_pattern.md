---
tag: code_problem
time_elapsed: 28
difficulty: easy
created: 2024-01-05T13:23
updated: 2024-01-05T14:25
---

# 290 - Word Pattern

**Notes**: This shouldn't have tooken me that long to figure out to be honest.

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:

    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts in completing this problem is that we had to use a map to map words to letters in the pattern. Then, if there are words that do no match the given pattern hash, we return false.

# Approach
<!-- Describe your approach to solving the problem. -->
I first made a condition where the pattern and the string of words have to be the same length. If they aren't, then there will never be a pattern.
Next, create a link between the letter and the word. If we encounter a letter that is not a key and a word that is not a value, we add it in the hash. Finally, if we encounter a letter that is in the map, BUT it does not equal the current word, then that means it's not following the pattern

# Complexity
- Time complexity: $O(n)$, we are looping over pattern once

- Space complexity: $O(n)$, we store our information within the `map` variable.


# Code
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # match each letter to a different word
        s = s.split(" ")

        # pattern and s have to be same length for anything to be true
        if len(pattern) != len(s):
            return False

        map = {}
        for i, letter in enumerate(pattern):
            if s[i] not in map.values() and letter not in map:
                map[letter] = s[i]

            # go through pattern, check if corresponding index in s matches
            # if not, then return false
            else:
                if map.get(letter) != s[i]:
                return False
        return True

```
