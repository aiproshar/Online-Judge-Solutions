'''
Updated cleanest solution
Multi Source BFS, we do modify the grid so no separate visited / parent relation data is needed
First push all the source in the queue, BFS guarantees we only need to update once
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        que = deque()
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == 0:
                    que.append((x,y))
        direction = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < len(rooms) and 0 <= ny < len(rooms[0]):
                    if rooms[nx][ny] == INF:
                        rooms[nx][ny] = rooms[x][y] + 1
                        que.append((nx, ny))

# Time Complexity: We visit each cell once, so its O(m*n)
# Space complexity: O(m*n), que can grow holding all elements, which is O(m*n)