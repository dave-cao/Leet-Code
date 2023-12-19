---
created: 2023-12-13T17:15
updated: 2023-12-18T14:58
tag: code_problem
time_elapsed: 6
difficulty: easy
---
## 217 - Contains Duplicate

**Time Elapsed: 6 minutes**
**Difficulty: Easy**

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

 

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts on completing this problem is to use something akin to a word counter. From there, if we found a word (or in this case a number) that has more than 1 count, then we can just return True.

# Approach
<!-- Describe your approach to solving the problem. -->
I used a map to store my numbers and their counts. Then, if we ever got a count that is higher then 1, then we return True. If we went the whole list without encountering a 2, then we return False.

# Complexity
- Time complexity: $$O(n)$$
    - As the input increases, the time it takes to complete this program will linearly increase
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
    - As the input increases, the size of the map will increase linearly (in the worst case where all values are distinct)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Checks if any number in nums appears twice. If there is a duplicate
        then return true, else return false"""

        # loop through every number and increment the map if it has the same value
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

            # if we find any map that has more than one occurence, then return True
            if num_map.get(num) > 1:
                return True
        return False

```

