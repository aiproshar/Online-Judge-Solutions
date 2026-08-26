class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        in_degree = {}
        out_degree = {}

        for i in range(1, n + 1):
            in_degree[i] = 0
            out_degree[i] = 0

        for x, y in trust:
            out_degree[x] += 1
            in_degree[y] += 1

        for i in range(1, n + 1):
            in_count = in_degree[i]
            out_count = out_degree[i]

            if out_count == 0 and in_count == n - 1:
                return i

        return -1

# Time Complexity: O(V+E)
# Space Complexity: O(V)