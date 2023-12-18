class Solution:
    def isSubsequence(self, s: str, t: str):
        # return true or false

        # The first thing we have to do is make sure that all the letters
        # in s are in t

        substring = [letter for letter in s]

        # loop through each letter in split_t and check to see if letter of split_s is there

        for letter in t:

            if substring:
                need_to_find = substring[0]
                if letter == need_to_find:
                    substring.pop(0)

        return not substring


s = Solution()
print(s.isSubsequence("abc", "acbcd"))
