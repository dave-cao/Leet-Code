---
tag: code_problem
time_elapsed: 13
difficulty: easy
process: better_way_to_do_this
created: 2023-12-25T19:01
updated: 2023-12-25T19:01
---

# 303 - Range Sum Query - Immutable

**Notes**: There is a better way to do this from [neetcode](https://www.youtube.com/watch?v=2pndAmo_sMA)
- basically you have to do some pre-processing of the nums array before you do the calculation and you can get an $O(1)$ time complexity. 
- If you reading this then this is your second time around. Try to find the answer.

Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

 

Constraints:

    1 <= nums.length <= 104
    -105 <= nums[i] <= 105
    0 <= left <= right < nums.length
    At most 104 calls will be made to sumRange.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
I think the hardest part about this problem was just figuring out what the question was asking of us. From a group of numbers (nums) get the sum of the range between two numbers. We have the range function in Python so this was pretty simple to do.

# Approach
<!-- Describe your approach to solving the problem. -->
Put the restraints in our range as left and right + 1 (because we want it to be both inclusive). Get the sum of that. Done.

# Complexity
- Time complexity: $O(n)$ ~ we loop the all the range worse case.


- Space complexity: $O(1)$ ~ we are storing data in only `total`.

# Code
```python
class NumArray:

    def __init__(self, nums: list[int]):
        self.range = nums

    def sumRange(self, left: int, right: int) -> int:

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(left,right)
        total = 0
        for i in range(left, right + 1):
            total += self.range[i]
        return total

```

