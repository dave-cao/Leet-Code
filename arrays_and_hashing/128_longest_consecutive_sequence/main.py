class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # BEST SOLUTION
        longest = 0
        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest

    def longestConsecutive_original(self, nums: list[int]) -> int:
        nums = sorted(list(set(nums)))
        print(nums)

        if not nums:
            return 0

        streak = 1
        current_streak = 1
        for i in range(len(nums) - 1):
            current = nums[i]
            next = nums[i + 1]

            if next == current + 1:
                current_streak += 1
            if next != current + 1 or (i == (len(nums) - 2)):
                if current_streak != 1:
                    if current_streak > streak:
                        streak = current_streak
                current_streak = 1
        return streak


def main():

    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))

    pass


if __name__ == "__main__":
    main()
