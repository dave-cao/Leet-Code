---
tag: code_problem
difficulty: medium
time_elapsed: 36
process: tutorial
created: 2024-01-14T09:22
updated: 2024-01-14T21:08
---

# 853 - Car Fleet

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
 

Constraints:

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Had to look at the solution before solving this one. I knew we had to use a stack here but not sure how exactly. However, it completely didn't cross my mind that we could just `sort` the array! If we sort it, then it'll be easy to pinpoint the cars and the cars that came before it. The deciding factor for these cars is the car in front of it. If the car in front gets to the finish line slower than any of the cars behind it, then the previous car will slow down to match the front car and it will become a fleet.

# Approach
<!-- Describe your approach to solving the problem. -->
First combine the position and speeds into tuples and then sort by position. After that, I create a stack and loop through the cars starting from the end. Then I calculate the time it takes for the distant car and put it in the stack. If the next cars (previous) are less than or equal to the are in front of it, then that means it will become a fleet with that car. We don't have to put it in the stack in that case! At the end, the amount of items in our stack is the number of car fleets that we have.

# Complexity
- Time complexity: $O(n \cdot log(n))$ ~ $2n$ to do two for loops, and $log(n)$ to sort

- Space complexity: $O(n)$ to store into our cars and stack

# Code
```python
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        # group the position and speed together
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        # sort the cars based on position
        cars.sort(key=lambda a: a[0])

        # intialize stack
        stack = []

        # go through the cars list backwards
        for i in range(len(cars) - 1, -1, -1):
            # grab our time needed to reach the finish line
            time = (target - cars[i][0]) / cars[i][1]

            # if there is nothing in our stack, then append (first car)
            # if a behind car takes longer to get to the finish line,
            # then it can't be a part of the fleet of the first position car
            # if all the cars are faster than the first car,
            # then the first car will be the deciding factor, and create a
            # single fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)

```
