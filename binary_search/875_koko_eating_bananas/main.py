import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = float("inf")

        while left <= right:

            mid = (right + left) // 2
            hours = self.get_hours(mid, piles)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        return result

    def get_hours(self, k, piles):
        # k is our eating speed
        result = 0
        for pile in piles:
            result += math.ceil(pile / k)
        return result


def main():
    piles = [3, 6, 7, 11]
    h = 8

    sol = Solution()
    sol.minEatingSpeed(piles, h)


if __name__ == '__main__':
    main()


# we need to figure out the minimum eating speed that she can
# have while still eating all the bananas before the guards return

# h / len(piles) == how long she has per pile to eat
# eg: 8 hours and 4 piles, then she has 2 hours per pile to eat

# therefore, we need to get the largest pile, and divide that by 2
# eg: ceil(11 / 2) = 6
# our limiting factor is our largest pile

# sort
# get largest number
