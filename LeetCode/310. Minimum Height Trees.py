'''
Brute Force Approach, TLE
We're running BFS for every node as a source, so its V(V+E)
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj_list = defaultdict(list)

        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        def bfs(source) -> int:
            que = deque([source])
            visited = {source}
            level = 0
            while que:
                current_width = len(que)
                level += 1
                for _ in range(current_width):
                    current = que.popleft()
                    for child in adj_list[current]:
                        if child not in visited:
                            visited.add(child)
                            que.append(child)
            return level - 1 # level - 1 is depth

        temp = []
        for source in range(n):
            height = bfs(source)
            temp.append((height, source))

        temp.sort()
        res = [temp[0][1]]

        for i in range(1, len(temp)):
            if temp[i - 1][0] == temp[i][0]:
                res.append(temp[i][1])
            else:
                break
        return res

# Time Complexity: O(V+E) -> O(2V) for each BFS, we run V times, so its  O(V^2), O(VlogV) for sorting
# Space Complexity: O(V+E) -> O(2V) -> O(V)
