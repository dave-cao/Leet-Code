class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        left_sum, right_sum = 0, sum(nums)

        for i, num in enumerate(nums):
            right_sum -= num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1


def main():
    sol = Solution()
    nums = [1, 7, 3, 6, 5, 6]
    nums = [1, 2, 3]
    nums = [2, 1, -1]
    print(sol.pivotIndex(nums))


if __name__ == "__main__":
    main()

# calculate the pivot index of thsi array
# - the index where the sum of all the numbers to the left of the index
# - is equal to the sum of all the numbers strictly to the index's right

# - start at the right most and the left most
