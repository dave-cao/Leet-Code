import time


class Solution:
    def findMin(self, nums: list[int]) -> int:
        # condition ends when left == right

        left, right = 0, len(nums) - 1
        minimum = nums[0]
        while left <= right:
            mid = (right + left) // 2
            # if our middle number is bigger
            # then we are in the left quadrant
            # so check the right quadrant
            if nums[mid] >= nums[0]:
                left = mid + 1
            # if our middle number is less
            # then we are in the right qudrant
            # so check the left quadrant
            elif nums[mid] < nums[0]:
                right = mid - 1
                minimum = min(minimum, nums[mid])
        return minimum


def main():
    sol = Solution()
    nums = [3, 1, 2]
    print(sol.findMin(nums))
    pass


if __name__ == "__main__":
    main()
