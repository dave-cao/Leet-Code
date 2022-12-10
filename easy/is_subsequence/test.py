class Solution:
    def isSubsequence(self, s: str, t: str):

        substring = [letter for letter in s]
        for letter in t:
            if substring:
                need_to_find = substring[0]
                if need_to_find == letter:
                    substring.pop(0)

        return not substring


s = Solution()
print(s.isSubsequence("abc", "ahbg"))
