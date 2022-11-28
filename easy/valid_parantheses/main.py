class Solution:
    def isValid(self, s: str):
        # return true or false

        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        # make sure each opening bracket has a closing bracket
        need_to_find = []
        for char in s:
            if char in brackets:
                # if you find an opening bracket, then append its closing bracket
                # to this list
                need_to_find.append(char)

                # check for adjacent brackets
            elif not need_to_find or brackets[need_to_find.pop()] != char:
                # if need_to_find is empty or closing bracket is not in order
                return False

        # return true if need_to_find is empty
        return not need_to_find


s = Solution()
print(s.isValid("()[]()"))

# This works because pop only does the most recent one, therefore,
# it will pop in order
# You can use pop or shift for order
