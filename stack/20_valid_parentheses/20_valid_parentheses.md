---
tag: code_problem
difficulty: easy
time_elapsed: 15
created: 2024-01-13T15:08
updated: 2024-01-13T15:08
---

# 20 - Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Pretty simple solution but you have to know what a stack is first! Basically when you make a parenthesis, it's only valid if the most recent opening bracket (last in) is matched first! (first out). 

# Approach
<!-- Describe your approach to solving the problem. -->
I used a stack, first, I matched any opening bracket, and put it in a stack. If it isn't an opening bracket, then it is probably a closing bracket. That closing bracket MUST be matched with the opening bracket at the beginning of the stack. If it doesn't match, then return False.

# Complexity
- Time complexity: $O(n)$ ~ we go through the whole string


- Space complexity: $O(n)$ ~ we put it in a stack

# Code
```python
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:
            # if char is an open bracket, then put in stack
            if char in brackets:
                stack.append(char)
            # otherwise, it's a closing bracket, so match with most recent
            # bracket
            else:
                # if not stack: too much to the right
                if not stack or brackets.get(stack.pop()) != char:
                    return False
        # case where too much on the left
        return not stack

```
