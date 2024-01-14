class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        stack = []
        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return result


def main():
    pass


if __name__ == '__main__':
    main()
