class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        num_stack = [temperatures[0]]
        i_stack = [0]
        output = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            temperature = temperatures[i]

            # if we found a temperature that is bigger than
            # our latest in the stack, update our output
            while num_stack and temperature > num_stack[-1]:
                num_stack.pop()
                prev_index = i_stack.pop()
                output[prev_index] = i - prev_index

            # input new temperature into stacks
            # and indices
            num_stack.append(temperature)
            i_stack.append(i)

        return output


def main():
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    sol.dailyTemperatures(temperatures)
    pass


if __name__ == "__main__":
    main()
