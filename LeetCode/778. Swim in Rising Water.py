'''
Prims Inspired / Min Heap Frontier
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        source = (0,0)
        heap = [(grid[0][0], source)]
        visited = set()
        direction = [
            (1,0),
            (0,1),
            (-1, 0),
            (0,-1)
        ]
        max_cost = 0
        while heap:
            cost, (x, y) = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            max_cost = max(max_cost, grid[x][y])
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                break
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if (nx, ny) not in visited:
                        heapq.heappush(heap, (grid[nx][ny], (nx,ny)))
        return max_cost


# Time Complexity: N^2.logE -> N^2logN
# Space: O(n^2)


'''
Came up with this when resolving
Dijkstra Variant with distance matrix
'''

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        time = [[math.inf] * len(grid[0]) for _ in range(len(grid))]
        time[0][0] = grid[0][0]
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        heap = [(time[0][0], 0, 0)]
        while heap:
            cost, x, y = heapq.heappop(heap)
            if cost > time[x][y]:
                # stale entry
                continue
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if time[nx][ny] > max(time[x][y], grid[nx][ny]):
                        time[nx][ny] = max(time[x][y], grid[nx][ny])
                        heapq.heappush(heap, (time[nx][ny], nx, ny))

        return time[len(time) - 1][len(time[0]) - 1]

# Time Complexity: n^2logn
# Space: N^2