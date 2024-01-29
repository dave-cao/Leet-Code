---
tag: code_problem
difficulty: medium
time_elapsed: 30
created: 2024-01-28T19:59
updated: 2024-01-28T19:59
---

# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Quick Notes

- This is a merge sort problem



---

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Felt like a merge sort problem. We could cut down the complexity time by looking for conditions if the smallest number in one array is bigger than the biggest number in the other array. Then we can just combine it directly.

# Approach
<!-- Describe your approach to solving the problem. -->
I basically just used merge sort to figure this out and then got the median from that.

# Complexity
- Time complexity: $O(n + m)$ ~ it aint $O(log(n + m))$

- Space complexity: $O(n)$ ~ we store a `merged_list` list.


# Code
```python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        merged_list = []
        if not nums1 and nums2:
            merged_list = nums2
        elif not nums2 and nums1:
            merged_list = nums1
        elif nums1[0] >= nums2[len(nums2) - 1]:
            # if the smallest number in nums1 is bigger
            # then the biggest number is num2, then all nums
            # in nums2 goes before nums1
            merged_list = nums2 + nums1
        elif nums1[len(nums1) - 1] <= nums2[0]:
            # if the largest number in nums1 is less than
            # the smallest number in nums2, then all nums in nums2
            # goes after nums1
            merged_list = nums1 + nums2
        else:
            # this is the the case where they have nums within each other
            # how do we merge them in O(log(n)) time?

            # lets just do merge sort first
            num1_pointer, num2_pointer = 0, 0

            while num1_pointer < len(nums1) and num2_pointer < len(nums2):
                num1 = nums1[num1_pointer]
                num2 = nums2[num2_pointer]

                # sort them in increasing order
                if num1 <= num2:
                    merged_list.append(num1)
                    num1_pointer += 1
                else:
                    merged_list.append(num2)
                    num2_pointer += 1

            # add the remaining numbers
            if nums1:
                while num1_pointer < len(nums1):
                    merged_list.append(nums1[num1_pointer])
                    num1_pointer += 1
            if nums2:
                while num2_pointer < len(nums2):
                    merged_list.append(nums2[num2_pointer])
                    num2_pointer += 1

        if merged_list and len(merged_list) % 2 == 0:
            # if the list is even
            # get the two mids within the list
            first_mid = merged_list[(len(merged_list) // 2) - 1]
            second_mid = merged_list[len(merged_list) // 2]
            median = (first_mid + second_mid) / 2

            return median
        else:
            median = merged_list[len(merged_list) // 2]
            return median

```
