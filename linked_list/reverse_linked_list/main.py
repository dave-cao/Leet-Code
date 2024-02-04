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
