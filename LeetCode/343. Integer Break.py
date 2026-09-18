class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(remain) -> int:
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            res = []
            for i in range(1, n):
                res.append(dp(remain - i) * i)
            return max(res)
        return dp(n)
# Time Complexity:  n states, n work each state. O(n^2)
# Space Complexity: O(n) recursion stack also cache