class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        # count numberes
        num_counter = count_nums(nums)

        # sort based on value
        num_counter = sorted(
            num_counter, key=lambda x: num_counter[x], reverse=True)

        # return the k most frequent elements
        return num_counter[:k]


def count_nums(nums):
    num_map = {}
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    return num_map


def main():

    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3]
    k = 2

    sol.topKFrequent(nums, k)


if __name__ == "__main__":
    main()
