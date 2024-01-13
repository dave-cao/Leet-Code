import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()
        left, right = 0, 0

        while right < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove left val from window
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1

            right += 1

        return output

    def maxSlidingWindow_v3(self, nums: list[int], k: int) -> list[int]:

        left, right = 0, 0
        max_num = float("-inf")
        max_nums = []
        max_index = -1
        while right < len(nums):
            num = nums[right]

            # keep track of the max so far
            if max_num < num:
                max_num = num
                max_index = right

            # limit the window to k
            if right - left + 1 == k:
                # input our maximum number so far
                max_nums.append(max_num)

                # if our left pointer is at the max so far
                # we want to pop it out
                if left == max_index:
                    # and reset our max nums
                    max_num = float("-inf")

                    # bring back our right pointer
                    # this might increase time complexity
                    right = left + 1
                left += 1
            else:
                right += 1
        return max_nums

    def maxSlidingWindow_v2(self, nums: list[int], k: int) -> list[int]:

        left = 0
        max_num = float("-inf")
        max_nums = []
        map = {}
        for right in range(len(nums)):
            num = nums[right]
            map[right] = num

            if num > max_num:
                max_num = num

            # if our window is at k
            if right - left + 1 == k:
                # get our max num so far and add to list
                max_nums.append(max_num)

                # shift our window from the left
                map[left] = float("-inf")

                # reset our max
                max_num = max(map.values())

                # update our left pointer by one
                left += 1
        return max_nums

    def maxSlidingWindow_naive(self, nums: list[int], k: int) -> list[int]:

        left = 0
        max_nums = []
        for right in range(k - 1, len(nums)):
            window = nums[left: right + 1]

            # get the max number from the window
            max_num = max(window)

            # put the max number into a list
            max_nums.append(max_num)

            left += 1
        return max_nums


def main():
    sol = Solution()
    nums = [1, -1]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))


if __name__ == '__main__':
    main()
