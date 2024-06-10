---
created: 2024-06-10T14:42
updated: 2024-06-10T14:42
---
# Problem 1: Contains Duplicate

[My Submission](https://leetcode.com/problems/contains-duplicate/submissions/1284245774/)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

# UMPIRE

## Understand

- What happens if we are given an empty array?
- What happens if we are given a single element?
- Is there a time constraint to solving this problem?
- Can we sort the array?

## Method

- hashmap

## Plan

It seems to me that the best way to implement this is to go through each
element in the array and count the number of elements in a map. If any of those elements are more than one, then return true. Otherwise return false.

```python

map = {}
for every num in nums:
    if num is not in map, then put it in map
    if num is in map, then return true!
At the end, if there is no return, then return false
```

## Implementation

```python
map = {}

for num in nums:
    if num in map:
        return True
    else:
        map[num] = None
return False
```

## Review
[LeetCodeLink](https://leetcode.com/problems/contains-duplicate/description/)

## Evaluate

Time complexity: $O(n)$ ~ because worse case all numbers are unique
Space complexity: $O(n)$ ~ because map increases with distinct input
