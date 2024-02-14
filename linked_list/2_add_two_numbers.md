---
tag: code_problem
time_elapsed: 22
difficulty: medium
---

# 2 - Add Two Numbers

## Quick Notes

- get the reversed of each linked list as a string, just continue adding to the front (gets reversed)
- you can add them and then create a new linked list in reverse order (if you keep adding to the front, it will be in reverse order)

---

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.


---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
First we need to get the numbers of each list in reversed order, add them and then create a new linked list in reverse order again.

# Approach
<!-- Describe your approach to solving the problem. -->
I created a helper function that would get the numbers in a linkedlist in reverse order as a string, then converted them to integers and reversed it back into a new linked list.

# Complexity
- Time complexity: $O(n)$

- Space complexity: $O(n)$ ~ we are creating a new list

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # get the numbers in reverse order as strings, then convert to numbers
        reversed_l1 = self.get_numbers_reversed(l1)
        reversed_l2 = self.get_numbers_reversed(l2)

        # add these two numbers together
        add_result = reversed_l1 + reversed_l2

        # convert back to a string (edge case if the number is too big)
        add_result = str(add_result)

        # store it in a linked list as integers reversed
        tail = ListNode(int(add_result[0]))
        head = tail
        for i in range(1, len(add_result)):
            value = int(add_result[i])

            # create a new node and point it to the tail
            add_node = ListNode(value, head)

            # set new placement of head
            head = add_node
        return head


    def get_numbers_reversed(self, head):
        current = head
        str_number = ""

        while current:
            str_number = str(current.val) + str_number
            current = current.next
        return int(str_number)
```
