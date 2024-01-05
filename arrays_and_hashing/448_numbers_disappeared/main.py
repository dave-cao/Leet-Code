class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # mark each number in its own array as negative if it exists
        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        # get only positives
        result = []
        for i, num in enumerate(nums):
            if num >= 0:
                result.append(i + 1)
        return result

    def findDisappearedNumbers_first(self, nums: list[int]) -> list[int]:
        map = set(i for i in range(1, len(nums) + 1))
        for num in nums:
            if num in map:
                map.remove(num)
        return list(map)


def main():
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDisappearedNumbers(nums))


if __name__ == "__main__":
    main()
