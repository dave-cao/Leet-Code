class Solution:
    def isValid(self, s: str):

        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        need_to_find = []
        for char in s:

            # is the character an opening bracket?
            if char in brackets:
                # save the closing bracket
                need_to_find.append(brackets[char])
            elif need_to_find and need_to_find.pop() == char:
                continue
            else:
                return False

        return not need_to_find


s = Solution()
print(s.isValid("()()(("))
