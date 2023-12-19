---
created: 2023-12-13T23:54
updated: 2023-12-18T14:58
tag: code_problem
time_elapsed: 7
difficulty: medium
---

# 347 - Top K Frequent Elements

**Time Elapsed**: 7 min
**Difficulty**: Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Intuitively, this was a pretty simple problem to solve. My first thoughts was to use a map as a number counter and from there, we sort the keys based on number count.

# Approach
<!-- Describe your approach to solving the problem. -->
I used a number counter map to count each number and then sorted that map based on the value of the counter. After that we just need to return a numbers from `0 - k`.

# Complexity
- Time complexity: $0(n)$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$0(n)$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # count numberes
        num_counter = count_nums(nums)

        # sort based on value
        num_counter = sorted(
            num_counter, key=lambda x: num_counter[x], reverse=True)

        # return the k most frequent elements
        return num_counter[:k]


def count_nums(nums):
    num_map = {}
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    return num_map

```
