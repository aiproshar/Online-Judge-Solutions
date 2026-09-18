class Solution:
    def numSquares(self, n: int) -> int:

        nums = []

        for i in range(1, math.isqrt(n) + 1):
            nums.append(i * i)

        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            for num in nums:
                if i + num <= n:
                    dp[i + num] = min(dp[i + num], dp[i] + 1)
                else:
                    break
        return dp[n]

# Time Complexity: O(n * sqrt(n))
# Space Complexity:  O(n)