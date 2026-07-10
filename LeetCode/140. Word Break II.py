"""
Backtrack solution, not optimal but works
No memoization, we pass the state all along
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []

        @cache
        def backtrack(start: int, state: tuple[str]):
            if start == len(s):
                sentence = " ".join(state)
                res.append(sentence)
            state = list(state)
            for i in range(start, len(s)):
                if s[start:i + 1] in wordDict:
                    state.append(s[start:i + 1])
                    backtrack(i + 1, tuple(state))
                    state.pop()

        backtrack(0, ())
        return res

# Time Complexity: O(2^N)
# Space: O(2^N)