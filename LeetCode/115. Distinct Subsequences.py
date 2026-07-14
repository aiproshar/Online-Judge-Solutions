'''
Top Down Approach + Memoization
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        @cache
        def dfs(i, j) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            ans = 0
            # current match, take it or try next
            if s[i] == t[j]:
                ans += dfs(i + 1, j + 1)
                ans += dfs(i + 1, j)
            # no match, go to next
            else:
                ans += dfs(i + 1, j)
            return ans

        return dfs(0, 0)
# Time Complexity: O(m*n) and also O(m+n) recursion stack
# Space Complexity: O(m*n) state space