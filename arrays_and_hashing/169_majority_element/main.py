class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        # create a counter, that counts
        # occurences of number
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1

        # get the map element that occurred
        majority_count = 0
        majority = 0
        for num, count in map.items():
            if count > majority_count:
                majority_count = count
                majority = num

        return majority


def main():
    sol = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    nums = [3, 2, 3]
    print(sol.majorityElement(nums))


if __name__ == "__main__":
    main()


# array of size n
# return the majority element
# what is the majority elemetn?
# - the element that appears more than floor(n / 2) times
# - a majority element always appears in the array


# Steps
# - first thought == we count the number of times a certain element
#   - is in an array
# - return the elemnt that is more than len(nums) // 2
# Steps
# - get the element that occurs the most and count it
# - the max() function will be useful here on map.values()
# - if that max element is mroe then len(nums), then return it
