---
tag: code_problem
time_elapsed: 80
difficulty: hard
created: 2023-12-18T11:40
updated: 2023-12-19T02:57
---

# 42 - Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 ![[42_trapping_rain_water-20231218114022245.jpg]]

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

 

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105

---

# My Thoughts

This question was pretty hard. It was a two pointer question but it wasn't very intuitive. You have to realize that for each bar, the maximum amount of water it can hold is the minimum between the max left so far bar and the max right so far bar. From there, you just subtract from the bar itself. If the resulting number is 0 or negative, then it doesn't hold water.

There's three different solutions that I have figured out.

1. Take slices of the left so far, right so far, and current bar. From there, get the max from the left and right, and then get the min between those two maxes. From there, you subtract the current height to get the amount of water it holds
2. Have an array hold the left max so far, another to hold right max so far, for each position. Then, we get the min from both and subtract from the current height. 
3. The actual two-pointer solution. We have one pointer at the beginning and another at the end. If left max is less than right max, we increase the left pointer. Note that here we are only concerned about the lesser pointer. I'm still not too sure about this solution so I will have to go back! TODO: pick apart this question again.

