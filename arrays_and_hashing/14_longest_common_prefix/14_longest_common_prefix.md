---
tag: code_problem
time_elapsed: 18
difficulty: easy
created: 2023-12-21T19:55
updated: 2023-12-21T19:55
---

# 14 - Longest Common Prefix

**Note**: Didn't need to look at solution for this problem :)

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts on this question was how on earth would we solve this with a time complexity if $O(n)$? The brute force method would be to get a word, and then compare it with every other word character by character.

# Approach
<!-- Describe your approach to solving the problem. -->
What I did was start with the first two words and get the common prefix between those two. That common prefix that we obtained is our new word to compare with the next word. And we just go on until we reach the end or there is no more common prefixes.

# Complexity
- Time complexity: $O(n * m)$ ~ because we have a double for loop. Time will increase by `len(list)` * `len(words)`. 

- Space complexity: $O(1)$ ~ because we are only storing one variable (common prefix)


# Code
```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # we begin by comparing the first word
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            current_string = strs[i]
            common = get_common(common_prefix, current_string)
            common_prefix = common

            # reduces runtime
            if common_prefix == "":
                return common_prefix

        return common_prefix


def get_common(word1, word2):

    # get the smaller word
    if len(word2) < len(word1):
        word1, word2 = word2, word1

    prefix = ""
    for i in range(len(word1)):
        word1_char = word1[i]
        word2_char = word2[i]

        if word1_char != word2_char:
            break
        else:
            prefix += word1_char

    return prefix

```
