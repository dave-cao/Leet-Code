class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        for i in range(len(nums * 1)):
            nums.append(nums[i])
        print(nums)
        return nums

    def getConcatenation_simple(self, nums: list[int]) -> list[int]:
        return nums * 2

    def getConcatenation_basic(self, nums: list[int]) -> list[int]:

        # we basically want to double the array
        new_nums = []
        for i in range(len(nums) * 2):
            if i > len(nums) - 1:
                i -= len(nums)

            new_nums.append(nums[i])

        return new_nums


def main():
    sol = Solution()
    nums = [1, 2, 1]
    sol.getConcatenation(nums)


if __name__ == "__main__":
    main()
