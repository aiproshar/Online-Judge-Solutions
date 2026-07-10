
'''
Top Down recursive DP

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        @cache
        def dp(start: int) -> bool:
            if start == len(s):
                return True
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    if dp(i+1) is True:
                        return True
            return False
        return dp(0)

# Time Complexity: O(N^3)
# Space: O(n)