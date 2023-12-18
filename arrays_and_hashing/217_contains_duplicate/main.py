class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """Checks if any number in nums appears twice. If there is a duplicate
        then return true, else return false"""

        # loop through every number and increment
        # the map if it has the same value
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

            # if we find any map that has more
            # than one occurence, then return True
            if num_map.get(num) > 1:
                return True
        return False


def main():

    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.containsDuplicate(nums))


if __name__ == "__main__":
    main()
