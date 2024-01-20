class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        stack = []  # stores (index, height)
        maxArea = 0

        # first run
        for i, height in enumerate(heights):
            # counts how many times we popped
            start = i
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                width = i - index
                area = h * width

                maxArea = max(maxArea, area)

                # set the start index back to the most recent pop's index
                start = index

            stack.append((start, height))

        if stack:
            for i, height in stack:
                width = len(heights) - i
                area = width * height
                maxArea = max(maxArea, area)
        return maxArea


def main():
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    heights = [3, 6, 5, 7, 4, 8, 1, 0]
    sol.largestRectangleArea(heights)


if __name__ == "__main__":
    main()
