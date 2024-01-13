---
tag: code_problem
difficulty: medium
time_elapsed: 15
created: 2024-01-13T15:37
updated: 2024-01-13T16:24
---

# 155 - Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Using python, the question is pretty trivial to implement a stack, however, the tricky part was the getMin function. We have to do this in O(1) time complexity. The trick here is to use ANOTHER stack that tracks the min values!

# Approach
<!-- Describe your approach to solving the problem. -->
I used another stack to track the min values. If a value is popped, then both the original stack and the min_stack are popped. This way, we can keep track of the current minimum, even if the current lowest value is popped out.

# Complexity
- Time complexity: $O(1)$ 

- Space complexity: $O(n)$

# Code
```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



```
