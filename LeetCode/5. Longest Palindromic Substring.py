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



# Greedy/Two pointer approach, even beats DP
# Expand around center, every palindrome has a center (single elem for odd, two for even palindrome)
# We pick every index and try to expand as far as we can
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = [0,0]
        def find(start, end):
            nonlocal pal
            if start < 0 or end >= len(s):
                return
            if s[start] == s[end]:
                if end - start > pal[1] - pal[0]:
                    pal = [start, end]
                find(start-1, end + 1)
        for i in range(len(s)):
            find(i,i)
            find(i, i+1)
        return s[pal[0]:pal[1] + 1]

# Time: O(n^2)
# Space: O(n) Recursion stack

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = [0, 0]

        for i in range(len(s)):
            start = i
            end = i

            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start > pal[1] - pal[0]:
                    pal = [start, end]
                start -= 1
                end += 1
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start > pal[1] - pal[0]:
                    pal = [start, end]
                start -= 1
                end += 1
        return s[pal[0]:pal[1] + 1]

# Time: O(n^2)
# Space: O(1)
