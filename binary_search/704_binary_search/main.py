class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            # 1 + ((right - left) // 2)
            mid = (right + left) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


def main():
    sol = Solution()
    nums = [5]
    target = 5
    print(sol.search(nums, target))


if __name__ == "__main__":
    main()
