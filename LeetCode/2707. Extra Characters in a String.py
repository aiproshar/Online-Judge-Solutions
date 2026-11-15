'''
Non Trie Based solution
We only jump if we can consume the words, so we only need to tract starting state
Two Choices, skip to take, take means consider it part of a word
Return min optimization
'''
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        @cache
        def dp(i) -> int:

            if i == len(s):
                return 0
            # skip the current char
            res = dp(i + 1) + 1

            for j in range(i, len(s)):
                if s[i:j + 1] in words:
                    res = min(res, dp(j + 1))
            return res

        return dp(0)


# Time Complexity: O(M*L + N * N * N), M = no of words, L = avg len, N = len(s).
# Space Complexity: M*L for dict, O(N) for @cache, O(N) recursive stack












