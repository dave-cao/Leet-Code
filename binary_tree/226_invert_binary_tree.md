---
tag: code_problem
time_elapsed: 10
difficulty: easy
---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
It's actually a pretty simple solution if you know how to implement an in-order traversal algorithm for a binary tree.

# Approach
<!-- Describe your approach to solving the problem. -->
I traversed the whole tree using in-order traversal, and when the algorithm sees that there is no right or left node, then switch then right and left node. Then go back up the call stack until it does it with every single node.

Return the root at the end.

# Complexity
- Time complexity: $O(n)$ ~ in-order traversal is an O(n) method

- Space complexity: $O(1)$ 

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Go to the deepest node and flip left and right
        # base case
        if root == None:
            return

        # traverse the whole tree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # only when both right and left are null, flip the
        # tree node
        root.left, root.right = root.right, root.left
 
        return root
        

        # use in-order traversal and do this to all nodes

        # flip left to right and right to left
```
