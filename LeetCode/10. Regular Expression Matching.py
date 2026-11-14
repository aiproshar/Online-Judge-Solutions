'''
True Hard, lot of back and forth with virtual interviewer
Solved almost 90% without any hint, the zero occurrence was missed
Also reaching end of s is okay, we can always burn remaining P if we have a *
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dp(i, j) -> bool:

            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if j + 1 < len(p) and p[j + 1] == "*":
                res = []
                res.append(dp(i, j + 2))
                if i < len(s):
                    if p[j] == '.' or p[j] == s[i]:
                        res.append(dp(i + 1, j))
                return any(res)

            if i == len(s):
                return False
            if s[i] == p[j] or p[j] == ".":
                return dp(i + 1, j + 1)
            return False

        return dp(0, 0)

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)