class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """Apparently this solution has shit runtime and memory"""
        for q, num1 in enumerate(nums1):
            # the number will auto be -1 to begin with
            nums1[q] = -1
            for i, num2 in enumerate(nums2):
                # if we find a bigger number, then set nums1 to that number
                if num1 == num2:
                    while i < len(nums2):
                        if nums2[i] > num1:
                            nums1[q] = nums2[i]
                            break
                        i += 1
        return nums1


def main():
    sol = Solution()
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    sol.nextGreaterElement(nums1, nums2)


if __name__ == "__main__":
    main()

# Understanding the problem
# - nums 1 is a subset of nums 2
# - when they say we have to get the next greater element
#  - we are given two arrays. num1 will be a subset of num2
#  - for each number in num1, we will search for that same number
#  - in num2. Then we get the next greater element in **nums2**

# Approaches
# - Brute
#   - for every number in nums1
#   - for every nubmer in nums2
#   - look for a match
#   - if there is a match, get the next greater element

# Solution
# - the solution is always coming from the reverse side
