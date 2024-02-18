---
tag: code_problem
difficulty: easy
time_elapsed: 4
---

# 141 - Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The premise of this question is to see if there is a cycle in a linked list. If there is a cycle within the linked list, then the **tail** must be the one with the cycle!

Thus, there can't be more than one cycle in a singly linked list.

# Approach
<!-- Describe your approach to solving the problem. -->
I created a map that kept track of the nodes. If I encountered a node already, then return True (there a cycle), however, if we go through the full linked list (it terminates) and we did not find a cycle then return false.

# Complexity
- Time complexity: $O(n)$ ~ worst case we go through the full linked list

- Space complexity: $O(n)$ ~ we are storing into a hashmap

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # keep track of all our nodes
        # once we have reached a node that we have grabbed before, then return true
        # if it terminates (reaches null) then return false
        map = {}
        current = head
        while current:
            if current not in map:
                map[current] = None
            else:
                return True
            current = current.next
        return False
        
```
