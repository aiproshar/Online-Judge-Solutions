
# Top Down recursive solution with memoization
# 99% same as : https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def countSubstrings(self, s: str) -> int:

        @cache
        def is_palindrome(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return is_palindrome(i + 1, j - 1)

        palindromes = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    palindromes += 1
        return palindromes

# Time Complexity: O(n^2)
# Space Complexity: O(n^2) + O(n) recursion stack

# Expand around center AKA bottom up
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Grows as long as its a palindrome
        def grow(i, j) -> int:
            total = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                total += 1
                i -= 1
                j += 1
            return total

        palindromes = 0
        for i in range(len(s)):
            # Odd palindromes
            palindromes += grow(i, i)
            # Even Palindromes
            palindromes += grow(i, i + 1)
        return palindromes

# Time: O(n^2)
# Space: O(1)
