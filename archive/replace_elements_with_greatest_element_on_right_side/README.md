---
created: 2024-02-04T12:50
updated: 2024-03-06T01:20
---
# 1299. Replace Elements with Greatest Element on Right Side

*Time*: 28 min 56 sec
*Video*: https://youtu.be/eo41dPNacSA

![question image](Permanent/Education/coding_interview/LeetCode/archive/replace_elements_with_greatest_element_on_right_side/img/image0.png)




## Explanation:
1. We are given an array of numbers
2. Starting from the left, we search all the elements to its right and see if
    there is any number greater than it
3. If there is, replace the current number with the greater number
4. Once you reach the last element, make it -1


## Battle Plan

1. We have to loop through the number array
2. How do we figure out a number and all its numbers to its right?
3. How do we compare a number and all it's numbers to the right?
4. My current thought process is to brute force it 

1. Starting from right
2. Store the current biggest starting from the right
3. Check to see if the left of the current number is larger or smaller
4. If smaller, then turn left number into right number
5. Continue down the route


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts on this problem was brute force. Make a double for loop that checks each advancing element if there is a bigger element. However, there should be a better way than that. Maybe storing the largest element and instead of starting left to right, let's go right to left!

# Approach
<!-- Describe your approach to solving the problem. -->
So to start, we will be going right to left. Since we want to track the largest numbers **to the right** of any element, if we *start* from the right, we have access to the currently largest number! However, we don't want to include the current number into our calculations, so therefore we must start to the right of the current number but not including the current number. From there, we will go down and check the largest number so far. If we reached a number larger than our largest number so far, then replace it to make it our new largest number. Then insert it into our new list. Otherwise, just insert the current largest number into our list.


# Code
```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        store_number = 0
        replaced_list = [-1]
        for i in range(len(arr) - 2, -1, -1):
            next_number = arr[i + 1]

            if next_number > store_number:
                store_number = next_number
                replaced_list.insert(0, store_number)
            else:
                replaced_list.insert(0, store_number)

        return replaced_list

```
