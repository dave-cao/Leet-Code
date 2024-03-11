---
tag: code_problem
difficulty: easy
time_elapsed: 10
---

# 104 - Maximum Depth of Binary Tree

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I would have to do depth-first search to figure out this problem.

# Approach
<!-- Describe your approach to solving the problem. -->
Go to the depths of both the left and right subtrees, and get the max of both. Return the maximum depth.

# Complexity
- Time complexity: $O(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(1)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        # do in-order traversal
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1

        return max(left_depth, right_depth)

        # keep track of largest distance?
        
```
