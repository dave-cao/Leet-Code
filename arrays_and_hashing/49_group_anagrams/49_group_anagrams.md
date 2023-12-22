---
created: 2023-12-13T18:30
updated: 2023-12-22T11:57
tag: code_problem
time_elapsed: 77
difficulty: medium
---

# 49 - Group Anagrams

**Time Elapsed**: 1 hr 17 min
**Difficulty**: Medium (when looking at the question it shouldn't be hard at all, but for some reason I just couldn't get a fast answer so I had to redo it multiple times.)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

---

# Intuition

My very first thought was to get the word count for each individual word, then compare each. When comparing, it they have the same word count, then append to a list within a map.

# Approach

I used the sorted() method to sort every string (since the string sorted will be the same order for every anagram). Then, I put the sorted word as the key within a map. If there is any other word with that same key, then append to a list of that key for the value. Done.

# Complexity
- Time complexity: O(n) (i think)
- Space complexity: O(n)

# Code
```python
class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # we can get the anagram by sorting
        map = {}
        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in map:
                map[sorted_string] = [string]
            else:
                map[sorted_string].append(string)

        return list(map.values())
```
