'''
I don't know why this is medium
We have no restriction on buy/sell, so we only do transaction on profit days

'''


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        profit = [0] * n
        for i in range(1, n):
            profit[i] = max(0, prices[i] - prices[i - 1])

        return sum(profit)
# Time Complexity: O(n)
# Space Complexity: O(n)