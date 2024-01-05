---
tag: code_problem
difficulty: easy
time_elapsed: 16
created: 2023-12-31T16:04
updated: 2023-12-31T16:46
---

# 1189 - Maximum Number of Balloons

**Optimal**:
- the optimal solution to completing this question would be to make two maps like I did. However, to take into account that balloon needs 2 "l" and 2"o"s, we need to get the ratio. As in for "l", it would be # of l's // 2.
- from there, we get the minimum so far.
- the ratio is important here

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 

Constraints:

    1 <= text.length <= 104
    text consists of lower case English letters only.

---

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts for this question was to save the characters within a map. 

# Approach
<!-- Describe your approach to solving the problem. -->
I created a character counter for the initial word given to us. Then, I continously loop through the word "balloon" and subtract from this counter until the counter reaches a negative number. If any letter reaches a negative number, then we can't spell balloon anymore.

# Complexity
- Time complexity: $O(n)$ ~ I feel like it's less then $O(n^2)$ but above $O(n)$. This is because at worst, the input string is just a bunch of 'balloonballoon'

- Space complexity: $O(n)$ ~ we are storing it in a single map

# Code
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # initialize char counter for balloon
        balloon_map = {}
        for char in "balloon":
            balloon_map[char] = balloon_map.get(char, 0) + 1

        # make a character counter for the given word
        map = {}
        for char in text:
            map[char] = map.get(char, 0) + 1

        # continously compare the balloon map with map, subtracting every time
        total = -1
        can_spell_balloon = True
        while can_spell_balloon:
            for char, count in balloon_map.items():
                # if the character exists, then see if we have enought
                if map.get(char):
                    map[char] = map.get(char) - count
                    if map.get(char) < 0:
                        can_spell_balloon = False
                        break
                # if it doesnt' exist, we can't spell balloon anyway
                else:
                    can_spell_balloon = False
                    break
            total += 1
        return total

```
