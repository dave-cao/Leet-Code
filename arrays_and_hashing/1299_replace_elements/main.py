class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        max_so_far = -1
        greatest = []
        for i in range(len(arr) - 1, -1, -1):
            greatest.insert(0, max_so_far)

            if arr[i] > max_so_far:
                max_so_far = arr[i]

        return greatest


def main():
    sol = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    sol.replaceElements(arr)


if __name__ == "__main__":
    main()
