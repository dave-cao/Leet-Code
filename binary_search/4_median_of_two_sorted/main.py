class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        merged_list = []
        if not nums1 and nums2:
            merged_list = nums2
        elif not nums2 and nums1:
            merged_list = nums1
        elif nums1[0] >= nums2[len(nums2) - 1]:
            # if the smallest number in nums1 is bigger
            # then the biggest number is num2, then all nums
            # in nums2 goes before nums1
            merged_list = nums2 + nums1
        elif nums1[len(nums1) - 1] <= nums2[0]:
            # if the largest number in nums1 is less than
            # the smallest number in nums2, then all nums in nums2
            # goes after nums1
            merged_list = nums1 + nums2
        else:
            # this is the the case where they have nums within each other
            # how do we merge them in O(log(n)) time?
            # is this O(log(n))?/????

            # lets just do merge sort first
            num1_pointer, num2_pointer = 0, 0

            while num1_pointer < len(nums1) and num2_pointer < len(nums2):
                num1 = nums1[num1_pointer]
                num2 = nums2[num2_pointer]

                # sort them in increasing order
                if num1 <= num2:
                    merged_list.append(num1)
                    num1_pointer += 1
                else:
                    merged_list.append(num2)
                    num2_pointer += 1

            # add the remaining numbers
            if nums1:
                while num1_pointer < len(nums1):
                    merged_list.append(nums1[num1_pointer])
                    num1_pointer += 1
            if nums2:
                while num2_pointer < len(nums2):
                    merged_list.append(nums2[num2_pointer])
                    num2_pointer += 1

        if merged_list and len(merged_list) % 2 == 0:
            # if the list is even
            # get the two mids within the list
            first_mid = merged_list[(len(merged_list) // 2) - 1]
            second_mid = merged_list[len(merged_list) // 2]
            median = (first_mid + second_mid) / 2

            return median
        else:
            median = merged_list[len(merged_list) // 2]
            return median


def main():
    sol = Solution()
    nums1 = [2]
    nums2 = []
    print(sol.findMedianSortedArrays(nums1, nums2))
    pass


if __name__ == "__main__":
    main()

# I think we have to do merge sort here (nvm)
# - merge sort is O(nlogn) time complexity (which is not good enough)

# case 1:
# - if the smallest number in nums1 is bigger than the largest
# - number in nums2, then we can just go nums2 + nums1

# case 2:
# - if the largest number in nums1 is less than the smallest number in
# nums2, then we can go nums1 + nums2
