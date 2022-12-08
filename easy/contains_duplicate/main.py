# Contains duplicate


class Solution:
    def containsDuplicate(self, nums: list):
        # returns true if list contains duplicate
        # false otherwise

        # go through the list

        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 0
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
