class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        BUY, SELL = 0, 1

        # returns cash amount we can make, net cash
        @cache
        def dp(i, state) -> int:
            if i >= len(prices):
                return 0
            res = []
            if state == SELL:
                # Sell now, cannot buy next day
                res.append(dp(i + 2, BUY) + prices[i])
                # We will take decision for sale tomorrow
                res.append(dp(i + 1, SELL))
            elif state == BUY:
                # Buy today
                res.append(dp(i + 1, SELL) - prices[i])
                # Take decision next day
                res.append(dp(i + 1, BUY))
            return max(res)

        return dp(0, BUY)

# Time Complexity: O(n)
# Space Complexity: O(n)
