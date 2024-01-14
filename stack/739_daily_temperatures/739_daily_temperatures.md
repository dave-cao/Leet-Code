---
tag: code_problem
difficulty: medium
time_elapsed: 31
created: 2024-01-14T08:32
updated: 2024-01-14T09:05
---

# 739 - Daily Temperatures

**Notes**: Solid question

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This uses stack somehow AND we have to somehow keep track of the indices that we are given! Usually with stack problems, if there are two things we need to keep track of, that means that we can use two stacks! We also use the subtraction of indices to get the distance between two different days.

# Approach
<!-- Describe your approach to solving the problem. -->
I had 2 stacks, a `num_stack` which kept track of our temperatures, and an `i_stack` which kept track of our indices. While we go through the temperatures, we will check the top of our stack to see if the current temperature is bigger than it. If it is, then we found one of our outputs. We can update the output using the indices from `i_stack`. We continually pop from our stack until either there is nothing left in the stack, or the top stack temperature isn't bigger than the current temperature. In that case, we just add the current temperature and index into our stacks.

# Complexity
- Time complexity: $O(n)$ ~ we go through the temperatures once

- Space complexity: $O(n)$ ~ storing our numbers into two stacks.

# Code
```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        num_stack = [temperatures[0]]
        i_stack = [0]
        output = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            temperature = temperatures[i]

            # if we found a temperature that is bigger than
            # our latest in the stack, update our output
            while num_stack and temperature > num_stack[-1]:
                num_stack.pop()
                prev_index = i_stack.pop()
                output[prev_index] = i - prev_index

            # input new temperature into stacks
            # and indices
            num_stack.append(temperature)
            i_stack.append(i)

        return output

```
