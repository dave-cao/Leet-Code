---
tag: code_problem
time_elapsed: 4
difficulty: easy
created: 2023-12-19T12:54
updated: 2023-12-19T12:54
---

# 1299 - Replace Elements with Greatest Element on Right Side

**Note**: Quite easy if we think of starting from the right side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

 

Constraints:

    1 <= arr.length <= 104
    1 <= arr[i] <= 105

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We need to keep track of the greatest numbers to its right. We can do that by starting at the right side!

# Approach
<!-- Describe your approach to solving the problem. -->
Start from the right end, then work your way down. If we encounter a bigger number, then set our max number to that bigger number. Append our biggest number to the list.

# Complexity
- Time complexity: $O(n)$
- Space complexity: $O(n)$

# Code
```python
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        max_so_far = -1
        greatest = []
        for i in range(len(arr) - 1, -1, -1):
            greatest.insert(0, max_so_far)

            if arr[i] > max_so_far:
                max_so_far = arr[i]

        return greatest

```
