---
tag: code_problem
time_elapsed: 15
difficulty: easy
---

# 100 Same Tree


Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false

---


# Solution
<!-- Describe your first thoughts on how to solve this problem. -->
I would have to use a traversal method using recursion and continously check both p and q. The only tricky part was when p is null and q is not or vice versa which we have to check within the base case.


# Complexity
- Time complexity: $0(n)$


- Space complexity: $O(n)$


# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True

        # check if values are the same
        if p.val != q.val:
            return False

        # check if left and right are mismatched
        left = self.isSameTree(q.left, p.left)
        right = self.isSameTree(q.right, p.right)
        return left and right

```
