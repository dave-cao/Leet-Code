class Solution:
    def maxArea(self, height: list[int]) -> int:

        # first make right and left pointers
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            x = right - left
            y = min(height[left], height[right])
            water = x * y

            if water > max_water:
                max_water = water

            if y == height[left]:
                left += 1
            else:
                right -= 1

        return max_water

    def brute(self, height: list[int]) -> int:
        max = 0
        for i in range(len(height)):
            for q in range(i + 1, len(height)):
                y = min(height[i], height[q])
                x = q - i
                water = x * y
                if water > max:
                    max = water

        return max


def main():
    sol = Solution()

    height = [1, 1]
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    print(sol.maxArea(height))


if __name__ == "__main__":
    main()
