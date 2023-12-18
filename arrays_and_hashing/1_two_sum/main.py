class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        word_map = {}
        # basically we are searching for the difference
        # of the numbers that we found already
        for i, num in enumerate(nums):
            if num in word_map:
                return [word_map[num], i]
            else:

                # target - num is key here
                # eg: if our target is 9 and our first element is 1,
                # then if we ever encounter an 8, then 1 + 8 = 9
                # omg this is so genius
                word_map[target - num] = i

    def two_sum_brute(self, nums: list[int], target: int) -> list[int]:

        for i, num in enumerate(nums):
            for q in range(i + 1, len(nums)):
                if num + nums[q] == target:
                    return [i, q]


def main():

    nums = [2, 7, 11, 15]
    target = 9

    sol = Solution()

    print(sol.twoSum(nums, target))

    pass


if __name__ == "__main__":
    main()
