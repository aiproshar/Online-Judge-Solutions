'''
Simple Dijkstra but not straightforward
Need to
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        m = len(heights)
        n = len(heights[0])
        effort = [[math.inf] * n for _ in range(m)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            _, x, y = heapq.heappop(heap)
            for dx, dy in direction:
                nx, ny = x+ dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if effort[nx][ny] > max(abs(heights[x][y] - heights[nx][ny]), effort[x][y]):
                        effort[nx][ny] = max(abs(heights[x][y] - heights[nx][ny]), effort[x][y])
                        heapq.heappush(heap, (effort[nx][ny], nx, ny))

        return effort[m - 1][n - 1]
# Here, V = m*n and E ~ V 
# Time Complexity: O(VlogV)
# Space: O(V)