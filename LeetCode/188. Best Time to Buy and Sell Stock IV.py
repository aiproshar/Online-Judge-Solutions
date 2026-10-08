

'''
General Template Solution for K transaction
'''
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        profit = [0] * len(prices)

        for i in range(1, len(prices)):
            profit[i] = prices[i] - prices[i - 1]

        BUY, SELL = 0, 1

        @cache
        def dp(i, t_completed, state):

            if i >= len(profit) or t_completed == k:
                return 0

            if state == BUY:
                # We can buy today or buy next day
                # As we not yet bought, no profit for tday (+/-)

                return max(dp(i + 1, t_completed, SELL), dp(i + 1, t_completed, BUY))
            elif state == SELL:
                # We can sell today or sell tomorrow
                # selling increases transaction count
                # As we have a stock bought we add todays profit, even if we sell today the profit adds up
                return max(dp(i + 1, t_completed + 1, BUY), dp(i + 1, t_completed, SELL)) + profit[i]

        return dp(0, 0, BUY)

# Time Complexity: O(n * K)
# Space Complexity: O(n * K)