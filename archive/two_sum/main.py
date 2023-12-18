class Solution:
    def twoSum(self, nums, target: int):
        # returns list of integers

        for i in range(len(nums) - 1):
            # longest solution
            for q in range(1, len(nums) - i):
                check = nums[i] + nums[q + i]
                print(check)
                if check == target:
                    return [i, q + i]

    def two_sum_2(self, nums, target):
        for i in range(len(nums) - 1):
            check = nums[i] + nums[(i + 1)]
            if check == target:
                return [i, i + 1]

    def two_sum_3(self, nums, target):
        # dictionary containing all the seen values
        # faster solution
        # peyman_np
        seen = {}

        for i, num in enumerate(nums):

            # find the number that adds up to target
            # we want to find x
            # remaining is a value
            remaining = target - num

            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[num] = i


solution = Solution()
print(solution.two_sum_3([3, 2, 4], target=6))
