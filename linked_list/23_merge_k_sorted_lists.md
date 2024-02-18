---
tag: code_problem
difficulty: hard
time_elapsed: 30
---

# 23 - Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We have to go through the first element of each list and get the smallest value. After that, once we got the smallest value, we update that specific list to the next pointer. End when we all the lists are now None.

# Complexity
- Time complexity: $O(n*m)$ ~ we have to go through each list, and for each of those lists, we go through each node vertically.

- Space complexity: $O(n)$

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # initiate a new linked list
        dummy = ListNode()
        tail = dummy

        while True:
            # gets the smalest value from all three lists
            smallest_so_far = ListNode(val=float("infinity"))
            index_to_update = -1
            for i, current_head in enumerate(lists):
                if current_head and smallest_so_far.val > current_head.val:
                    smallest_so_far = current_head
                    index_to_update = i

            # now we have a smallest so far, we need to update it to the next pointer in that specific list
            if index_to_update != -1:
                lists[index_to_update] = lists[index_to_update].next

            # append the smallest so far to a new linked list
            tail.next = smallest_so_far
            tail = tail.next

            # check to see if all nodes in lists are None
            count = 0
            for node in lists:
                if not node:
                    count += 1
            if count == len(lists):
                break

        return None if dummy.next.val == float("infinity") else dummy.next 

            





        return None
```
