# classic BFS with multi-source 
# two separate visited set
# Kind of backtracking, we go up from water, instead going down from every cell (which may not result in going water at all, computation waste)
# O (M*N) with optimization, if we grow, we grow only once (added to ocea), or we dont grow and stop at O(1)
class Solution:
    def __bfs(self, i, j, heights: list[list[int]], ocean: set):

        #first optimization
        #If its already reaching to ocean, we dont need to do this again. The multi-source was already explored
        # This reduces from (m+n)(m*n) -> m*n: Linear time complexity
        if (i, j) in ocean:
            return 
        que = deque()
        que.append((i, j))
        print(que)
        visited = {(i, j)}
        ocean.add((i, j))

        while que:
            x, y = que.popleft()
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]):
                    if (nx, ny) not in visited and heights[nx][ny] >= heights[x][y]:
                        visited.add((nx, ny))
                        ocean.add((nx, ny))
                        que.append((nx, ny))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        self.pacific = set()
        self.atlantic = set()

        #Pacific
        for j in range(len(heights[0])):
            self.__bfs(0, j, heights, self.pacific)

        for i in range(len(heights)):
            self.__bfs(i, 0, heights, self.pacific)
        # Atlantic
        # Tricky part
        for j in range(len(heights[0])):
            self.__bfs(len(heights) - 1, j, heights, self.atlantic)
        for i in range(len(heights)):
            self.__bfs(i, len(heights[0]) - 1, heights, self.atlantic)
        ans_set = self.pacific & self.atlantic

        ans_list = list(ans_set)

        return ans_list
