---
tag: code_problem
time_elapsed: 28
difficulty: medium
---

# 19 - Remove Nth Node From End of List

## Quick Notes

- get the length of the linkedlist and subtract it from n to get the actual index we want to remove from
- from there it is a simple linked list removal

---

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This is a simple removal problem. The trick is in the beginning where you want to get the length of the linked list first.

# Approach
<!-- Describe your approach to solving the problem. -->
I first got the length of the list, then subtracted it from `n` to get the amount of nodes we need to traverse to actually remove the node. Then removed it.

# Complexity
- Time complexity: $O(n)$ ~ simply because we had to get the length of the linked list

- Space complexity: $O(1)$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the length of the linkedlist
        # the new n will be length - n
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next

        reversed_n = length - n
        
        # case when head is the element to be removd
        if reversed_n == 0:
            head = head.next
            return head
        
        # move the current pointer to the 
        # node previous to the one that needs
        # to be removed
        current = head
        for i in range(reversed_n - 1):
            # if head.next is null, then the range doesn't exist
            if current.next == None:
                return head
            current = current.next

        # if current.next.next exists, you can skip over
        if current.next and current.next.next:
            current.next = current.next.next
        else:
            # if it doesn't exist, then we are 
            # removing the tail of the linkedlist
            current.next = None

        return head

# if head == value, then head = head.next

# we can just loop through the list with a for loop
# if node == None, then it doesn't exist and we break
# otherwise, we found it

# once we find it
# we want to stop when node.next = val
# if node.next.next exists, then node.next = node.next.next

# otherwise, if it doesn't exist,
# then we set node.next to None
```
