---
tag: code_problem
time_elapsed: 20
difficulty: easy
created: 2024-02-11T16:42
updated: 2024-02-11T16:42
---

# 21 - Merge Two Sorted Lists

## Quick Notes
- regularly merge two sorted lists
- time complexity: $O(n + m)$
- space complexity: $O(1)$

---

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
First we would need two different pointers, and then a new dummy node to add the nodes to. I drew it out and it was a lot easier to understand that way.

# Approach
<!-- Describe your approach to solving the problem. -->
Do a regular merged sort but update a linkedlist instead.

# Complexity
- Time complexity: $O(n + m)$

- Space complexity: $O(1)$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        list1_current = list1
        list2_current = list2

        # new head
        new_head = ListNode()
        current_new_head = new_head

        while list1_current is not None and list2_current is not None:
            if list1_current.val <= list2_current.val:
                current_new_head.next = list1_current

                list1_current = list1_current.next
            else:
                # list 2 is less than list one
                current_new_head.next = list2_current

                list2_current = list2_current.next

            # update the new head to next node
            current_new_head = current_new_head.next

        # add the straglers
        if list1_current:
            current_new_head.next = list1_current
        elif list2_current:
            current_new_head.next = list2_current
        return new_head.next

```
