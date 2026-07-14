'''
Top Down Recursive DFS + Memoization
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dfs(i, j) -> int:
            if i == len(word1) and j == len(word2):
                return 0
            if i != len(word1) and j == len(word2):
                return dfs(i + 1, j) + 1
            if i == len(word1) and j != len(word2):
                return dfs(i, j + 1) + 1

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            res = []
            if word1[i] != word2[j]:
                res.append(dfs(i + 1, j))
                res.append(dfs(i, j + 1))
                res.append(dfs(i + 1, j + 1))
            return min(res) + 1

        return dfs(0, 0)


# Time Complexity: O(m*n)
# Space Complexity: State Space + Recursion Depth: O(m*n) + O(m+n)