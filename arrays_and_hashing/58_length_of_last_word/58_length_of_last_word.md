---
tag: code_problem
time_elapsed: 5
difficulty: easy
created: 2023-12-20T15:53
updated: 2023-12-20T20:42
---

# 58 - Length of Last Word

**Note**: Perhaps this one was too easy.

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My very first thoughts was that we had to start from the end of the string and work our way backwards. Once we reach an empty string, then thats the end of the word.

# Approach
<!-- Describe your approach to solving the problem. -->
I started at the end of the string. From there, we simply counted any non-white space characters until we reached another whitespace. If we did, then that's the end of the word. We also had to take into account for trailing whitespace, thus, our condition only ends if our length also has some count in it, because that means the beginning whitespace have already been skipped.

# Complexity
- Time complexity: $O(n)$ ~ we loop through all of `s` in the worst case scenario 
- Space complexity: $O(1)$ ~ the only variable we are using to store space is `length`.


# Code
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            elif length:
                return length

        return length

```
