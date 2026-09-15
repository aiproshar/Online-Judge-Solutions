# DP top down solution
# We generate all possible substring and check each for palindrome
# Keep track of largest length and substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        @cache
        def is_palindrome(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return is_palindrome(i + 1, j - 1)

        longest = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if is_palindrome(i, j):
                    if j - i + 1 > len(longest):
                        longest = s[i:j + 1]
        return longest

# Time Complexity: O(n^2)
# Space complexity: O(n^2), with O(n) recursion depth



# Greedy/Two pointer approach, even beats DP
# Expand around center, every palindrome has a center (single elem for odd, two for even palindrome)
# We pick every index and try to expand as far as we can
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j) -> list[int]:
            res = [0, 0]
            while i >= 0 and j < len(s) and s[i] == s[j]:
                res = [i, j]
                i -= 1
                j += 1
            return res

        longest = [0, 0]

        for k in range(len(s)):
            # Odd Palindrome
            i, j = expand(k, k)
            if (j - i + 1) > (longest[1] - longest[0] + 1):
                longest = [i, j]
            # Even Palindrome
            i, j = expand(k, k + 1)
            if (j - i + 1) > (longest[1] - longest[0] + 1):
                longest = [i, j]
        return s[longest[0]:longest[1] + 1]

# Time: O(n^2)
# Space: O(1)