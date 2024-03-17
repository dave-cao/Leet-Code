---
tag: code_problem
time_elapsed: 19
difficulty: medium
---

# 235 - Lowest Common Ancestor of a Binary Search Tree

# Approach
Not the most elegant of solutions but it works. First I got all the ancestors of each `p` and all the ancestors of `q` and put them into two different lists. Then starting from right to left, I would check if they have a common ancestor, if they do, then return that ancestor!

The tricky part was figuring out how to get the all the ancestors of a node. I used a combination of both pre-order traversal and post-order traversal. In pre-order traversal, I appended nodes into a list, and using post-order, I would pop the last node out, ultimately giving me an single ancestral like tree every time. Then when I found the node I wanted, I would return and stop the recursion.

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(n)$

# Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the lowest common ancestor is the lowest node that both p and q share as an ancestor

        # Grab all the ancestors of both p and q and put it into separate lists
        ancestors_p = []
        ancestors_q = []

        self.findAncestor(root, p, ancestors_p)
        self.findAncestor(root, q, ancestors_q)

        # starting from right to left, see if they have any common ancestors
        for i in range(len(ancestors_p) - 1, -1, -1):
            ancestor = ancestors_p[i]
            if ancestor in ancestors_q:
                return ancestor


    def findAncestor(self, root, node, ancestor_list):

        if not root:
            return

        # in pre-order traversal, append nodes into a list
        ancestor_list.append(root)

        # stop traversal if we found our node
        if root.val == node.val:
            return ancestor_list

        left = self.findAncestor(root.left, node, ancestor_list)
        right = self.findAncestor(root.right, node, ancestor_list)

        if left or right:
            return ancestor_list

        # get rid of paths that we have already traversed
        ancestor_list.pop()

```
