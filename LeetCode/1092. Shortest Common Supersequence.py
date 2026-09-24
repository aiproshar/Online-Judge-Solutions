'''
Top Down Recursive DP
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        @cache
        def dp(i, j) -> deque:
            if i == len(str1) and j == len(str2):
                return deque([])

            elif i == len(str1):
                temp = dp(i, j + 1).copy()
                temp.appendleft(str2[j])
                return temp

            elif j == len(str2):
                temp = dp(i + 1, j).copy()
                temp.appendleft(str1[i])
                return temp
            else:
                if str1[i] == str2[j]:
                    # optimization, this is we need to maximize
                    temp = dp(i + 1, j + 1).copy()
                    temp.appendleft(str2[j])
                    return temp
                else:
                    first = dp(i + 1, j).copy()
                    first.appendleft(str1[i])
                    second = dp(i, j + 1).copy()
                    second.appendleft(str2[j])
                    return first if len(first) <= len(second) else second

        return "".join(dp(0, 0))
# Time Complexity, m*n states, m+n work in each state. (m+n) * mn
# Space Complexity: (m+n) * mn, we get MLE