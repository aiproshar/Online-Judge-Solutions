
# Top Down recursive solution with memoization
# 99% same as : https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        
        def isPalindrome(i,j):
            if dp[i][j] != None:
                return dp[i][j]
            if i >= j:
                dp[i][j] = True
                return dp[i][j]
            if s[i] == s[j] and isPalindrome(i + 1, j - 1):
                dp[i][j] = True
                return dp[i][j]
            else:
                dp[i][j] = False
                return dp[i][j]
        
        count = 0

        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j) is True:
                    count +=1
        return count

# Time and space complexity: O(n^2)
