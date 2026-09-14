class Solution:
    def tribonacci(self, n: int) -> int:

        #1. Objective Function dp(x) returns nth tribonacchi sequence number
        @cache
        def dp(n):
            # 2. Base Cases
            if n < 3:
                return int(n > 0)
            # 3. Recurrence Relation
            return dp(n-1) + dp(n-2) + dp(n-3)
        #4. Order of Computation. + 5.Where is the answer
        return dp(n)
# Time Complexity: O(n)
# Space Complexity: O(n) recursion depth



class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return int(n > 0)

        dp = [None] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
# Time Complexity: O(n)
# Space Complexity: O(n), no call stack overflow risk