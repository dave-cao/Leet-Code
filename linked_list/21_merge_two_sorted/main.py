# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def main():
    sol = Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    sol.mergeTwoLists()


if __name__ == "__main__":
    main()
