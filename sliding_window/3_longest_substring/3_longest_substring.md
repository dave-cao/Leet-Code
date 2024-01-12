---
tag: code_problem
time_elapsed: 42
difficulty: easy
created: 2024-01-11T19:46
updated: 2024-01-11T20:34
---

# 3 - Longest Substring Without Repeating Characters

**Notes:** AND HE FIGURES IT OUT AFTER 42 MINUTES

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Two different thought processes I had while solving this problem. One, I needed to store the variables that I found in some sort of hashmap or list. Two, I would need two pointers.

# Approach
<!-- Describe your approach to solving the problem. -->
First, I initialize two pointers, and constantly update the right pointer. If by any chance, the right pointer is the same as the left pointer, then that is our substring. Thus, we can shift our left pointer to the right by one. Then we move our right pointer back beside our left pointer. However, there is an edge case for something like "abcb". This method doesn't check for similarities within each string, thus we need to use a hashmap to check for this. 

# Complexity
- Time complexity: $O(n)$ ~ since we are only using one for loop

- Space complexity: $O(n)$ ~ we store our inputs into map

# Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if empty string, then there is no max count
        if not s:
            return 0

        # pointers
        left_index = 0
        right_index = 1

        # counter variables
        count = 1
        max_count = 1

        # map
        map = {}

        # create two pointers
        while right_index < len(s):
            # if the left and right pointer are not the same
            # then update the right pointer and count by 1
            if s[left_index] != s[right_index] and not map.get(s[right_index]):
                # keep track of letters traversed
                map[s[right_index]] = 1

                count += 1
                right_index += 1

            # otherwise, they are not the same, then update
            # the left pointer and put the right pointer beside the left
            # and reset the count to 0
            else:
                map = {}
                left_index += 1
                right_index = left_index + 1
                count = 1

            # if ever, the count is more then the max count
            # then update the max count
            if count > max_count:
                max_count = count
        return max_count


```
