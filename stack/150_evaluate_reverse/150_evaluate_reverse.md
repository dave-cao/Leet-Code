---
tag: code_problem
time_elapsed: 33
difficulty: medium
created: 2024-01-13T16:51
updated: 2024-01-13T17:39
---

# 150 - Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Another pretty simple stack problem. The tricky part for me was actually the division!

# Approach
<!-- Describe your approach to solving the problem. -->
Keep on appending numbers (if its not an operation), to the stack, once we find an operation, then take the recent 2 items in the stack and do the operation on them, and then put it back in the stack.

# Complexity
- Time complexity: $O(n)$ ~ going through tokens once

- Space complexity: $O(n)$ ~ storing data into a stack

# Code
```python
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {
            "+": lambda num1, num2: num1 + num2,
            "-": lambda num1, num2: num1 - num2,
            "/": lambda num1, num2: int(num1 / num2),
            "*": lambda num1, num2: num1 * num2,
        }

        for token in tokens:
            # if the token is not an operation
            # then it is a number to put in our stack
            if token not in operations:
                stack.append(int(token))
            # otherwise, take the top two of the stack and use the
            # operation
            else:
                # get the last two nums from our token list
                num2 = stack.pop()
                num1 = stack.pop()

                # grab the operation function
                operation = operations.get(token)

                # place the resulting number into our stack
                stack.append(operation(num1, num2))

        return stack[-1]


```

