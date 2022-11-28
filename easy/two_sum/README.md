# Two Sum

*Time to Completion*: 32 min 2 sec
*Video*: https://youtu.be/zT2u4gMKM3w

## Documentation of Process


### Run Down

nums = [1, 2, 3]
target = int

return indices of the two numbers such that they add up to target

Example:
```Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
---

Is there a case where an output would not be serial?

In that case, we would have to do check:
```
0 1
0 2
0 3
1 2
1 3
2 3
```
Something like the above

We would have to make a double for loop.

Eg:
```
nums = [2, 7, 11, 15]
for i, each number:
    we have to check other number on it
    first round
    i = 0
    check i == i + 1
    check i == i + 2
    check i == i + 3
    
    i = 1
    second round
    check i == i + 1
    check i == i + 2
    
    i = 2
    third round
    check i == i + 1
    
    for q in range(1, len(nums) - i)
        check each iteration to see if they add to target
        if so, then output indices == [i, q]



```
