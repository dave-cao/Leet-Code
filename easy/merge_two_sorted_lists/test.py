# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = ListNode()

    def append(self, node):
        cur = self.head
        new_node = ListNode(node)

        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

    def display(self):
        cur = self.head

        nodes = []
        while cur.next is not None:
            cur = cur.next
            nodes.append(cur.val)

        print(nodes)


class Solution:
    def mergeTwoLists(self, list1, list2):

        head_one = list1
        head_two = list2

        new_head = cur = ListNode()

        while head_one and head_two:

            if head_one.val < head_two.val:
                cur.next = head_one
                head_one = head_one.next

            else:
                # head_two.val is smaller
                cur.next = head_two
                head_two = head_two.next

            cur = cur.next

        if head_one:
            cur.next = head_one
        if head_two:
            cur.next = head_two
        nodes = []
        while new_head.next is not None:
            new_head = new_head.next
            nodes.append(new_head.val)

        print(nodes)


ll_one = Linked_list()
ll_two = Linked_list()

ll_one.append(1)
ll_one.append(2)
ll_one.append(3)

ll_two.append(4)
ll_two.append(5)
ll_two.append(6)

s = Solution()
s.mergeTwoLists(ll_one.head.next, ll_two.head.next)
