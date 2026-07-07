'''
Recursive Approach
'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# Time Complexity: Tree Depth N, two choices. So 2^n
# Space: Recursion O(n)

# With memoization
class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# Time: O(n)
# Space: O(n)
'''
Iterative DP, bottom up approach
Start From base case, buildup to real problem
'''
class Solution:
    def fib(self, n: int) -> int:

        if n == 0 or n == 1:
            return n

        dp = [None] * (n + 1)
        dp[1] = 1
        dp[0] = 0
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# Time: O(n)
# Space: O(n)

'''
Space optimized final solution
We stop here
'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        prev_2 = 0   # fib(i-2)
        prev_1 = 1   # fib(i-1)
        for i in range(2, n + 1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return prev_1

# Time: O(n)
# Space: O(1)