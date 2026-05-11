# dumbfuck bruteforce approach
# if we buy today compare profit on every possible future day
# Store max, local maxima -> global maximum
# TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                # readability >> python oneliners in any universe
                # Code is written for humans, not for machine
                current_profit = prices[j] - prices[i]
                max_profit = max(current_profit, max_profit)
        return max_profit

# time complexity: O(n^2)
# space complexity: O(1)


# This is maximum subarray sum in disguise
# We need to find the subarray with max sum, typically it's the whole sum but we have negatives here
# Kadane's algorithm, either we continue growing the previous subarray, or we start subarray from us
# We need to calculate which path is optimized, gives us DP vibes
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        profits = [0] * n

        for i in range(1, n):
            profits[i] = prices[i] - prices[i - 1]

        previous_profit = 0
        max_profit = 0
        for i in range(1, n):
            current = max(previous_profit + profits[i], profits[i])
            max_profit = max(max_profit, current)
            previous_profit = current
        return max_profit
# Time complexity: O(n)
# Space complexity:O(n)

# Can we do it in constant space ?
# Of course, our profit is stateless, its always remains the same
# We can compute this on the fly
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        running_profit = 0
        max_profit = 0
        for i in range(1, n):
            # these names make more sense
            # running profit, todat/daily profit more meaningful
            profit_today = prices[i] - prices[i - 1]
            running_profit = max(running_profit + profit_today, profit_today)
            max_profit = max(max_profit, running_profit)
        return max_profit
# time complexity: O(n)
# space complexity: O(1)





