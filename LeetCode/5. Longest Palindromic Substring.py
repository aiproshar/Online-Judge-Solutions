# Dumbfuck bruteforce
# We generate all possible substring and check each for palindrome
# Keep track of largest length and substring

class Solution:
    def isPalindrome(self, s) -> bool:
        return s == s[::-1]
            
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_str = ""

        # N^2 loop, generate all possible substring (inclding single char)
        for i in range(len(s)):
            for j in range(i, len(s)):
                #This is the edge case, its more likely related to python
                # str[i:j] means before j, so if we really want upto j, we need to use j+1
                if self.isPalindrome(s[i: j + 1]) is True:
                    if j - i + 1 > max_len:
                        max_len = max(max_len, j - i + 1)
                        max_str = s[i:j + 1]
        return max_str

# Time Complexity: O(n^3)
# Space complexity: O(n)


# DP solution, the hardest problem is figuring out subproblem
# If i -> j is a substring, i+1, j-1 is also a substring
# We can memoize 2D dp table, if s[i:j] is a palindrome
class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]

        def isPalindrome(s, i, j) -> bool:
            if dp[i][j] != None:
                return dp[i][j]
            if i >= j:
                dp[i][j] = True
                return dp[i][j]

            if isPalindrome(s, i + 1, j - 1) is True and s[i] == s[j]:
            # Optimization: lazy checking s[i] == s[j] first to avoid unnecessary recursive calls
                dp[i][j] = True
            else:
                dp[i][j] = False
            return dp[i][j]

        max_len = 0
        max_str = ""
        # Generate all possible substring
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s, i, j) is True:
                    if j - i + 1 > max_len:
                        max_len = max(max_len, j - i + 1)
                        max_str = s[i : j + 1]
        return max_str

# Time Complexity: O(n^2)
# Space complexity: O(n^2) //2D dp table

# TODO: We are doing useless substring copy, we really dont need that
# Similar Problem with much cleaner solution: https://leetcode.com/problems/palindromic-substrings/submissions/1869753324/
# 99% similar, instead of traking the longest palindrome, we count total palindromes number YaY





### More Cleaner Version of previous code

class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]

        def isPalindrome(i, j) -> bool:
            if dp[i][j] != None:
                return dp[i][j]
            if i >= j:
                dp[i][j] = True
                return dp[i][j]

            if s[i] == s[j] and isPalindrome(i + 1, j - 1) is True:
                dp[i][j] = True
            else:
                dp[i][j] = False
            return dp[i][j]

        max_len = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j) is True:
                    if j - i + 1 > max_len:
                        max_len = max(max_len, j - i + 1)
                        max_str_idx = (i, j + 1)
        max_str = s[max_str_idx[0]:max_str_idx[1]]
        return max_str


# Greedy/Two pointer approach, even beats DP
# Expand around center, every palindrome has a center (single elem for odd, two for even palindrome)
# We pick every index and try to expand as far as we can
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        p_len = 0
        p_idx = ()

        # Handling the odd palindromes
        for idx in range(n):

            i = idx
            j = idx

            while 0 <= i < n and 0 <= j < n:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            i += 1
            j -= 1
            if j - i + 1 > p_len:
                p_len = j - i + 1
                # Python slice goes before, not upto
                p_idx = (i, j + 1)


        # Handling the even palindromes
        # Corner case : We use two char as center, so handle out of bound issues
        for idx in range(n - 1):

            i = idx
            j = idx + 1

            while 0 <= i < n and 0 <= j < n:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break
            i += 1
            j -= 1
            if j - i + 1 > p_len:
                p_len = j - i + 1
                # Python slice goes before, not upto
                p_idx = (i, j + 1)
        return s[p_idx[0] : p_idx[1]]

                