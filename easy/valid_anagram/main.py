class Solution:
    def isAnagram(self, s: str, t: str):

        # loop through and store all letters in first string
        seen_one = {}
        seen_two = {}

        for letter in s:
            seen_one[letter] = seen_one.get(letter, 0) + 1

        for letter in t:
            seen_two[letter] = seen_two.get(letter, 0) + 1

        return seen_one == seen_two


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
