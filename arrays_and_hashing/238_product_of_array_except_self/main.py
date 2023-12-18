class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = 1
        postfix = 1
        result = [0] * n

        # store the prefix first
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # multiply the now stored prefix by the postfix
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


def main():
    nums = [1, 2, 3, 4]

    sol = Solution()
    sol.productExceptSelf(nums)

    pass


if __name__ == "__main__":
    main()
