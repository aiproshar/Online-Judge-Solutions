'''
Top Down recursive + memo
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dp(i, j) -> int:
            if i == len(word1) and j == len(word2):
                return 0
            # Corner Case, parking at end of string
            # What if we reached end of one, but not other. In that case we can
            # Add / remove other so it may also reaches the park
            if i > len(word1) or j > len(word2):
                return math.inf

            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            else:
                res = []
                # insert
                res.append(dp(i, j + 1) + 1)
                # delete
                res.append(dp(i + 1, j) + 1)
                # replace
                res.append(dp(i + 1, j + 1) + 1)
            return min(res)

        return dp(0, 0)

# Time Complexity: O(m*n)
# Space Complexity: State Space + Recursion Depth: O(m*n) + O(m+n)