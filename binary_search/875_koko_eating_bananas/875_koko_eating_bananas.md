---
tag: code_problem
time_elapsed: 15
process: tutorial
difficulty: medium
---

# 875. Koko Eating Bananas
<https://leetcode.com/problems/koko-eating-bananas/>

## Quick Notes

- binary search on eating speed rather than piles
- the range of eating speed will go from 1 to the largest pile
- we will use binary search to get the eating speed
- shift the left pointer if the eating speed is too long
- shift the right pointer if the eating speed is too short

---

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
This question was quite hard to think of intuitively. We have to first think about the brute force solution. Test every single eating speed until the max number of bananas. However, we can use binary search ON THAT brute force solution to optimize it.

# Approach
<!-- Describe your approach to solving the problem. -->
The range we are doing our binary search on will be from 1 - largest pile. Then we just have to get the number of hours for each pile. If an eating speed is too long (more than h), then shift the left pointer (because everything before that will be too long). If it is less than or equal to "h", we shift the right pointer to the left to see if we can go any slower.

# Complexity
- Time complexity: $O(m log(n))$

- Space complexity: $O(1)$

# Code
```python
import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = float("inf")

        while left <= right:

            mid = (right + left) // 2
            hours = self.get_hours(mid, piles)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result

    def get_hours(self, k, piles):
        # k is our eating speed
        result = 0
        for pile in piles:
            result += math.ceil(pile / k)
        return result

```
