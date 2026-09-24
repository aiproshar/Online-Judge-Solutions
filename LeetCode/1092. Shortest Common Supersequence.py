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


'''
Same idea, but we dont store the path anymore, we construct it
We calculate length and store the Shortest Common Length and store
Then we use this info to dind out the optimal path
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        @cache
        def dp(i, j) -> str:
            if i > len(str1) or j > len(str2):
                return math.inf
            if i == len(str1) and j == len(str2):
                return 0

            elif i == len(str1):
                return dp(i, j + 1) + 1

            elif j == len(str2):
                return dp(i + 1, j) + 1
            else:
                if str1[i] == str2[j]:
                    # optimization, this is we need to maximize
                    return dp(i + 1, j + 1) + 1
                else:
                    return min(dp(i + 1, j), dp(i, j + 1)) + 1

        dp(0, 0)
        res = []
        i = j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                res.append(str1[i])
                i += 1
                j += 1
            elif dp(i + 1, j) <= dp(i, j + 1):
                res.append(str1[i])
                i += 1
            else:
                res.append(str2[j])
                j += 1
        while i < len(str1):
            res.append(str1[i])
            i += 1
        while j < len(str2):
            res.append(str2[j])
            j += 1
        return "".join(res)


# Time Complexity: O(mn)
# Space Complexity: O(mn)