---
tag: code_problem
time_elapsed: 23
difficulty: easy
---

# 572 - Subtree of Another Tree

## Quick Notes
- find the node within the root that matches with the subRoot node
- then compare if both of them are the same tree
- there may be multiple nodes that match the subRoot node, so we have to check all of them

# Approach
This is very similar to the `SameTree` problem but with a few extra steps. First, we need to find the node within the root that matches with the subRoot node. Then we just compare if both of them are the same tree, if not, then return false.

The tricky part of this question is the first part, how do we find the node within the root that matches with the subRoot node? You basically have to match every single node with the subRoot node, if the values match, then see if they are the same tree. I split this up into 2 helper functions. 

# Complexity
- Time complexity: $O(n)$ ~ we use dfs here

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the node that is similar to the subroot
        return self.findNode(root, subRoot)

    def isSameTree(self, root_1, root_2):
        if not root_1 and not root_2:
            return True
        if not root_1 or not root_2:
            return False
        if root_1.val != root_2.val:
            return False

        
        left = self.isSameTree(root_1.left, root_2.left)
        right = self.isSameTree(root_1.right, root_2.right)
        return left and right


    def findNode(self, root, subRoot):
        if not root:
            return

        left = self.findNode(root.left, subRoot)
        right = self.findNode(root.right, subRoot)

        if left or right:
            return root

        # post order traversal so we can find the latest node
        if root.val == subRoot.val:
            if (self.isSameTree(root, subRoot)):
                return True
        
```
