class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        count = 0
        for i in range(len(flowerbed)):
            left, right = i - 1, i + 1

            if flowerbed[i] == 1:
                continue

            left_flower = 0 if left < 0 else flowerbed[left]
            right_flower = 0 if right >= len(flowerbed) else flowerbed[right]

            if left_flower == 0 and right_flower == 0:
                count += 1
                flowerbed[i] = 1

        return count >= n


def main():
    flowerbed = [0, 0, 0, 0, 0, 0, 0, 1, 1]
    n = 1
    sol = Solution()
    sol.canPlaceFlowers(flowerbed, n)
    pass


if __name__ == "__main__":
    main()

# we need to count the amount of valid spaces inside a flowerbed
# first check if a spot is empty. Then check the left and right of it.
# if either left or right is filled, then can't put flower in there
