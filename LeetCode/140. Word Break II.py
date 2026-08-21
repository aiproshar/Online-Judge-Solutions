"""
Backtrack solution, not optimal but works
No memoization, we pass the state all along
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        wordDict = set(wordDict)
        def backtrack(start_, current):

            if start_ == len(s):
                res.append(" ".join(current))
                return
            for i in range(start_, len(s)):
                if s[start_ : i + 1] in wordDict:
                    current.append(s[start_ : i + 1])
                    backtrack(i + 1, current)
                    current.pop()
            return
        backtrack(0, [])
        return res

# Time Complexity: O(2^N)
# Space: O(2^N)

'''
This was notoriously difficult, more difficult than any problem i ever solved
And python list reference and caching on top made things worse
Had to take a debuger/print help, but that will not be available in pressure cooker test
Dont know how its possible to come up to this solution clean on pen.paper
Took 1 hour with debugger/print help
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordDict = set(wordDict)

        @cache
        def backtrack(start_) -> list[list]:

            if start_ == len(s):
                return [[]]
            res = []
            for i in range(start_, len(s)):
                if s[start_ : i + 1] in wordDict:
                    partials = backtrack(i + 1)
                    pre = s[start_ : i + 1]
                    for partial in partials:
                        temp = [pre]
                        temp.extend(partial)
                        res.append(temp)
            return res


        res = backtrack(0)
        return [" ".join(x) for x in res]
# Time Complexity: O(n) states, on each state n loop and copy overhead, so its O(n^3)
# Space: O(n), at top we can have the sentence broken into n different distinct words n dofferent eays
# So its O(n^2)


'''
This is still not optimal, there is a TRIE solution that is more elegant, will do later
'''