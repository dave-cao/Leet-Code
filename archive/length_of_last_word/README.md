# 58. Length of Last Word

- *Time*: 7 min 7 sec
- *Video*:

![question image](img/image0.png)

What do we know?
1. We are given a string with words and spaces, we want to return the length of
    the last word
2. First, we have to realize that a string may contain multiple spaces within in


Plan:
1. Split the string into individual elements separated by spaces
2. Loop through that list, and see if it is a space or not...Or use the strip()  method?

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The first thing I thought of was to separate the string into it's individual elements, take the last element of that, and then get the length of that.

# Approach
<!-- Describe your approach to solving the problem. -->
At first, I thought of using the `.strip()` method, however the `.split()` method will create a list of the string while getting rid of all white space! How cool is that! From there, you can access the last element of the array by getting it's `[-1]` index. Then use the `len()` method to get the length of it. Done.

# Code
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        return len(s.split()[-1])
```
