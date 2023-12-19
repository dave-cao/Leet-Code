---
tag: code_problem
time_elapsed: 7
difficulty: easy
created: 2023-12-16T11:47
updated: 2023-12-18T14:58
---

# 125 - Valid Palindrome

**Time Elapsed**: 7 minutes
**Difficulty**: easy

*This question was pretty easy*

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The very first thing I thought of when making a solution to this problem was to simply grab the reversed string and compare it with the original string. If they match, then it is a palindrome.

# Approach
<!-- Describe your approach to solving the problem. -->
The first thing we have to figure out is what symbols are allowed within this solution. From looking at the cases, it seems like only alphabetical and numerical values are allowed. Good thing python has an `isalnum()` function to check just this! 

# Complexity
- Time complexity: $O(n)$
    - this is because we use a single for loop

- Space complexity: $O(n)$
    - the strings will increase in memory as the input increases.

# Code
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        reversed = ""
        for i in range(len(s)):
            start = s[i].lower()
            end = s[len(s) - 1 - i].lower()

            if start.isalnum():
                forward += start
            if end.isalnum():
                reversed += end

        return forward == reversed

```
