class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:
            # if char is an open bracket, then put in stack
            if char in brackets:
                stack.append(char)
            # otherwise, it's a closing bracket, so match with most recent
            # bracket
            else:
                # if not stack: too much to the right
                if not stack or brackets.get(stack.pop()) != char:
                    return False
        # case where too much on the left
        return not stack


def main():
    sol = Solution()
    s = "())}"
    print(sol.isValid(s))
    pass


if __name__ == '__main__':
    main()
