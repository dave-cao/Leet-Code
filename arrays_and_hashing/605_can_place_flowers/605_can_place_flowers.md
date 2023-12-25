---
tag: code_problem
time_elapsed: 26
difficulty: easy
created: 2023-12-24T13:35
updated: 2023-12-24T14:15
---

# 605 - Can Place Flowers

**Notes**: Shouldn't have taken this long to complete

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length


---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Intuitively this was pretty easy to understand. I just needed to get a left and right pointer, and check to see if both of them are empty. If they are, then we can place a flower.

# Approach
<!-- Describe your approach to solving the problem. -->
I did exactly what I described in my intuition. Had two pointers for the left and right of my current index. Check if they were both equal to 0 and then planted.

# Complexity
- Time complexity: $O(n)$ ~ we iterate over this for loop


- Space complexity: $O(1)$ ~ we only store into count


# Code
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        count = 0
        for i in range(len(flowerbed)):
            left, right = i - 1, i + 1

            if flowerbed[i] == 1:
                continue

            left_flower = 0 if left < 0 else flowerbed[left]
            right_flower = 0 if right >= len(flowerbed) else flowerbed[right]

            if left_flower == 0 and right_flower == 0:
                count += 1
                flowerbed[i] = 1
        return count >= n
```
