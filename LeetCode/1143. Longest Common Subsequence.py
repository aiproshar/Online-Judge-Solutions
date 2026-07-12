'''
Top Down Recursive + Memoization
Only drawback: If m+n > 1K default python call stack overflow

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return dp( i +1, j+ 1) + 1

            return max(dp(i + 1, j), dp(i, j + 1))

        return dp(0, 0)

# Time Complexity: O(m*n) + O(m+n) call stack
# Space: O(m*n)

