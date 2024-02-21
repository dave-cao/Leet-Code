---
tag: code_problem
time_elapsed: 52
difficulty: hard
---

# 25 - Reverse Nodes in k-Group

## Quick Notes

- split the linked list into multiples of `k`
- reverse each of those
- connect them together

---

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
First, we would need to split up the linked lists into multiples of `k`, reverse each of those, and then return the new reversed linked list.

# Approach
<!-- Describe your approach to solving the problem. -->
I split up the linked lists into multiples of `k`, and put it in a list. Then for each head in the list, I reversed it and replaced the head with the new head. Then I connected each of those linked lists together.

# Complexity
- Time complexity: $O(n^2)$ ~ we are doing a double loop

- Space complexity: $O(n)$ ~ we create a list
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # split up the linked lists into groups of k in a list (the tail of each will point to None)
        # append the heads into a list
        # split lists will be a tuple of (head, tail)
        lists = [head]
        current = head
        i = 0
        while current:
            next = current.next
            if (i + 1) % k == 0:
                # current is the tail here (if we ever need it)
                current.next = None
                lists.append(next)

            i += 1
            current = next

        # now lists has split heads in multiples of k
        # then we go through each linked list and reverse them (easy leetcode question)
        for i, list_head in enumerate(lists):
            list_head = self.reverse_list(list_head, k)
            lists[i] = list_head

        # connect the linked lists together again
        # we need to get the tail of a certain head
        for i in range(len(lists) - 1):
            # get the tail
            current_list = lists[i]
            current_tail = self.get_tail(current_list)

            next_list = lists[i + 1]
            current_tail.next = next_list
        return lists[0]


    def get_tail(self, head):
        current = head
        while current.next:
            current = current.next
        return current

            


    def reverse_list(self, head, k):

        # don't reverse when length of list is less than k
        # get length
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        if length < k:
            return head

        # otherwise, reverse it
        current = head
        next, previous = None, None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
