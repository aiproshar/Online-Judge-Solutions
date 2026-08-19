

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        def backtrack(idx, current):

            if idx == len(s):
                res.append(current.copy())
            for i in range(idx, len(s)):
                if s[idx:i+1] == s[idx:i+1][::-1]:
                    current.append(s[idx:i+1])
                    backtrack(i+1, current)
                    current.pop()
        backtrack(0, [])
        return res
# Time Complexity: T(n) = T(n-1) + T(n-2) + .... T(0)
# This merges to 2^N,  we have copy overhead of N so  TC: O(N* 2^N)
# Space Complexity: all possible subset , 2^N and we can have upto N len each subset, so N*2^N, call stack of O(n)
