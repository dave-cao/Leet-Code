```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        new = ListNode(0, head)

        # get the tail
        tail = head
        while tail.next is not None:
            tail = tail.next

        while (tail != head):
            current = head
            head = head.next
            current.next = tail
            current = tail

            # set new tail
            temp = head
            while temp.next is not None and temp.next.next is not None:
                temp = temp.next
                
            tail = temp
            tail.next = None

            # case where current = head
            # this part took me so long to figure out
            if current != head:
                current.next = head


        return new.next
```
