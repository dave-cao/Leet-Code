class Solution:
    def trap(self, height: list[int]) -> int:
        # Best solution O(1) memory
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        result = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

        return result

    def trap_better_solution(self, height: list[int]) -> int:
        # O(n) memory
        # get max left
        max_left = []
        current_max_left = 0
        for i in range(len(height)):
            max_left.append(current_max_left)
            if height[i] > current_max_left:
                current_max_left = height[i]

        # get max right
        max_right = []
        current_max_right = 0
        for i in range(len(height) - 1, -1, -1):
            max_right.insert(0, current_max_right)
            if height[i] > current_max_right:
                current_max_right = height[i]

        # get water
        total_water = 0
        for i in range(len(height)):
            water = min(max_left[i], max_right[i]) - height[i]

            if water > 0:
                total_water += water
        return total_water

    def trap_my_solution(self, height: list[int]) -> int:
        water_trapped = 0
        for i in range(len(height)):
            # slice it into 3 different arrays
            previous = height[:i]
            next = height[i + 1:]
            current = height[i]

            if previous:
                previous = max(previous)
            else:
                previous = 0
            if next:
                next = max(next)
            else:
                next = 0

            water = min(previous, next) - current
            if water > 0:
                water_trapped += water
        return water_trapped


def main():
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    sol.trap(height)


if __name__ == "__main__":
    main()

# how do we know when two bars contain water within them?
# get our starting block, and then continously find another block that is
# bigger than it
