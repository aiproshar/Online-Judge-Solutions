

'''
Top Down Recursive DP
We need to use all elements strictly, if len do not add up do early termination
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def dp(i, j) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            res = []
            if i != len(s1) and s1[i] == s3[i+j]:
                res.append(dp(i+1, j))
            if j != len(s2) and s2[j] == s3[i+j]:
                res.append(dp(i, j+1))
            return any(res)
        return dp(0,0)
# Time Complexity: O(m*n) state space, O(m+n) recursion depth
# Space Complexity: O(m*n) memo