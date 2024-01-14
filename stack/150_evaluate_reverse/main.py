class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {
            "+": lambda num1, num2: num1 + num2,
            "-": lambda num1, num2: num1 - num2,
            "/": lambda num1, num2: int(num1 / num2),
            "*": lambda num1, num2: num1 * num2,
        }

        for token in tokens:
            # if the token is not an operation
            # then it is a number to put in our stack
            if token not in operations:
                stack.append(int(token))
            # otherwise, take the top two of the stack and use the
            # operation
            else:
                # get the last two nums from our token list
                num2 = stack.pop()
                num1 = stack.pop()

                # grab the operation function
                operation = operations.get(token)

                # place the resulting number into our stack
                stack.append(operation(num1, num2))

        return stack[-1]


def main():
    sol = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    tokens = ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/", "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60", "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*",
              "180", "70", "-40", "-", "*", "86", "132", "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28", "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-", "-59", "+", "187", "-", "143", "/", "-79", "-89", "+", "-"]

    print(sol.evalRPN(tokens))
    pass


if __name__ == "__main__":
    main()
