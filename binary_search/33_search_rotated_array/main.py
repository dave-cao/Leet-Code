class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        first_num = nums[0]
        while left <= right:
            mid = (right + left) // 2
            mid_num = nums[mid]
            right_quad = target < first_num

            # current quadrant is left quad
            if mid_num >= first_num:

                # if the target is in the right quad
                # and we are in the left quad, then go to the right
                if right_quad:
                    left = mid + 1
                # if the target is in the left quad
                # and we are in the left quad, then do regular binary search
                else:
                    # then do regular binary search
                    if mid_num < target:
                        left = mid + 1
                    elif mid_num > target:
                        right = mid - 1
                    else:
                        return mid

            # current quadrant is right quad
            elif mid_num < first_num:

                # if the target is in the right quad
                # and we are in the right quad
                if right_quad:
                    # then do regular binary search
                    if mid_num < target:
                        left = mid + 1
                    elif mid_num > target:
                        right = mid - 1
                    else:
                        return mid
                else:
                    # otherwise, go to the left quad
                    right = mid - 1
        return -1


def main():
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    nums = [3, 1]
    target = 1
    print(solution.search(nums, target))
    pass


if __name__ == "__main__":
    main()
