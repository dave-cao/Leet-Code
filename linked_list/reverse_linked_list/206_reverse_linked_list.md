---
tag: code_problem
difficulty: easy
time_elapsed: 10
---

# 206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
First thought here was that we need 3 different pointers and to continually update it. The other trick is to start our previous and next to null.

# Approach
<!-- Describe your approach to solving the problem. -->
Set three pointers. After we switch an arrow, we update our previous to current, and current to next.

# Complexity
- Time complexity: $O(n)$ ~ traverse the whole list once
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # this is the recursive solution
        # base case
        if (head is None or head.next is None):
            return head

        # recursively reverse the rest of the list
        reversedHead = self.reverseList(head.next)

        # a way to break down the solution
        head.next.next = head
        head.next = None

        return reversedHead

    def reverseList_iterative(self, head: ListNode) -> ListNode:

        current = head
        previous = next = None

        while current is not None:
            # set next pointer to next node
            next = current.next

            # switch the pointer to previous node
            current.next = previous

            # update previous to current
            previous = current

            # update current to next node
            current = next

        return previous


# 1 -> 2 -> 3 -> 4 -> null

```
