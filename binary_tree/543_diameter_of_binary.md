---
tag: code_problem
time_elapsed: 37
difficulty: easy
created: 2024-03-10T18:28
updated: 2024-03-11T10:58
---

# 543 - Diameter of a Binary Tree

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first intuition is that we would need to get the addition between the max depth of the right and left subtrees of any node. And then we get the one with the largest length. The trickiest part would be how to keep track of the max length via recursion.

# Approach
<!-- Describe your approach to solving the problem. -->
I made a separate function to get the maximum depth. Then I traversed each node and got the max length for each node and saved it within `self.max_diameter`. Then I just returned max_diameter.

# Complexity
- Time complexity: $O(n^2)$ ~ we do two traversals

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we have to get the maximum left and right subtree of every single node
        self.max_diameter = 0

        return self.getDiameter(root)

    def getDiameter(self, root):
        if not root:
            return 0

        # post order traversal
        self.getDiameter(root.left)
        self.getDiameter(root.right)

        # for the current node, go left and right
        max_left = self.getMaxDepth(root.left)
        max_right = self.getMaxDepth(root.right)

        total = max_left + max_right

        if total > self.max_diameter:
            self.max_diameter =  total

        return self.max_diameter



    def getMaxDepth(self, root: Optional[TreeNode]) -> int:
        # gets the maximum depth of a given node
        if not root:
            return 0
        max_left = self.getMaxDepth(root.left) + 1
        max_right = self.getMaxDepth(root.right) + 1

        return max(max_left, max_right)
        
```
