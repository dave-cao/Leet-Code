class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)

        triples = []
        for i in range(len(nums)):
            current_num = nums[i]

            if i > 0 and nums[i - 1] == current_num:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:

                sum = current_num + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    triple = [current_num, nums[left], nums[right]]
                    triples.append(triple)
                    left += 1
                    print(nums[left], nums[left - 1])
                    while left > 0 and nums[left] == nums[left - 1]:
                        left += 1

        return triples


def main():

    sol = Solution()
    nums = [0, 1, 1]
    nums = [0, 0, 0]
    nums = [-1, 0, 1, 0]
    nums = [-2, 0, 1, 1, 2]
    nums = [3, -2, 1, 0]
    nums = [0, 0, 0, 0]
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))

    pass


if __name__ == "__main__":
    main()
