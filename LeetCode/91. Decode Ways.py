class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        dec = {str(i) for i in range(1, 27)}

        @cache
        def dp(idx) -> int:
            if idx == len(s):
                return 1
            # take one
            total = 0
            if idx < len(s) and s[idx:idx + 1] in dec:
                total += dp(idx + 1)

            # take two
            if idx + 1 < len(s) and s[idx:idx + 2] in dec:
                total += dp(idx + 2)
            return total

        return dp(0)

# Time Complexity: O(n) -> Recursion depth
# Space Complexity: O(n)