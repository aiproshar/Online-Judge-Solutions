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



'''
Trie + DP
The harder variant and more efficient
Instead of taking every substring and trying to see if its on a dict, a trie works on fail fast model
If we walk down and stuck, that means we wont be able to match any further word
Also no overhead of copy/slice
'''
class Node:
    def __init__(self, key=None):
        self.key = key
        self.childs = {}
        self.is_end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        root = Node()

        # Build the Trie
        for word in dictionary:
            current = root
            for ch in word:
                if ch not in current.childs:
                    current.childs[ch] = Node()
                current = current.childs[ch]
            current.is_end = True

        @cache
        def dp(i) -> int:
            if i == len(s):
                return 0
            # skip the current char
            res = dp(i + 1) + 1

            current = root
            for j in range(i, len(s)):
                if s[j] not in current.childs:
                    break
                else:
                    current = current.childs[s[j]]
                    if current.is_end:
                        res = min(res, dp(j + 1))
            return res

        return dp(0)

# Time Complexity: m = number of words L = avg len,N = len(s).  TC: O(N^2 + M * L). M*L -> Trie Build
# Space Complexity: O(N + M * L)