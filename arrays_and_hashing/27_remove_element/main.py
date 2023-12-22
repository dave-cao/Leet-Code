class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == val:
                nums.pop(i)
                nums.append("_")
            elif num == "_":
                break
            else:
                i += 1
        return i


def main():

    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    nums = [0, 1, 3, 3, 3, 0, 4, 3]
    val = 2
    print(sol.removeElement(nums, val))

    pass


if __name__ == "__main__":
    main()
