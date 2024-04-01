---
tag: code_problem
time_elapsed: 49
difficulty: medium
---

# 102 - Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

# Approach
<!-- Describe your approach to solving the problem. -->
Use breadth first search here. So we have a marked set and a to_explore queue. Continue exploring and popping out from to_explore until it is empty. 

The trick here is that we want to get the size of our current depth! To do that, we just get the length of our to_explore list! Once we get all the neighbors of all the nodes within our depth, then all the nodes in our to_explore is now all the nodes within the next depth!

# Complexity
- Time complexity: $O(n^2)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$O(n^2)$
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we want to get the breadth first search of these nodes
        if not root: return []

        # will hold the marked nodes
        marked = set()
        marked.add(root)

        # will hold the nodes to explore
        to_explore = [root]

        # testing list
        result = [[root.val]]

        while (to_explore):
            level_size = len(to_explore) #size of current depth

            # stores all nodes within this level
            level_nodes = []
            for i in range(level_size):

                # explore left and right of current node
                current = to_explore.pop(0)

                for node in self.getLeftRight(current):
                    if (node not in marked):
                        marked.add(node)
                        to_explore.append(node)
                        level_nodes.append(node.val)
            if level_nodes: result.append(level_nodes)
        return result
 




    def getLeftRight(self, root):
        neighbors = []
        if root.left: neighbors.append(root.left)
        if root.right: neighbors.append(root.right)
        return neighbors
```
