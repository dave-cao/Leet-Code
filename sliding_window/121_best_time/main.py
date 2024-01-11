class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        left_index = 0
        right_index = 1
        max_profit = 0
        while right_index < len(prices):
            profit = prices[right_index] - prices[left_index]

            if profit < 0:
                left_index = right_index
                right_index = left_index + 1
            else:
                if profit > max_profit:
                    max_profit = profit
                right_index += 1
        return max_profit

    def maxProfit_naive(self, prices: list[int]) -> int:
        """TIME LIMIT EXCEEDED"""

        # store max profit that we make
        max_profit = 0

        # for each day
        for i in range(len(prices)):
            starting = prices[i]
            # for each subsequent day after the day we are looking at
            for q in range(i + 1, len(prices)):
                # get the profit
                profit = prices[q] - starting

                # update our profit counter to get max profit
                if profit > max_profit:
                    max_profit = profit
        return max_profit


def main():
    sol = Solution()
    prices = [7, 6, 4, 3, 1]
    prices = [7, 1, 5, 3, 6, 4]
    sol.maxProfit(prices)
    pass


if __name__ == "__main__":
    main()

# we have to find the max so far, and then the lowest so far

#
