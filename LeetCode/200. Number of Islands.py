
#Basic BFS variation
# We calculate the children of a parent on the fly, based on 2D grid variation
# Change the board to mark visited board cells


class Solution:

	def __bfs(self, i, j, grid: list[list[str]]) -> None:
		queue = deque()
		queue.append((i, j))
		grid[i][j] = "0"

		# This is important, we must write clean and easy to explain code
		# Instead of writing 4 If logics, we define the direction matrix and iterate over it
		direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
		while queue:
			x, y = queue.popleft()
			for dx, dy in direction:

				# Another clean code example
				# dx, dy -> Its difference or delta. Good convention
				# nx, ny -> nex x and new y, this is adding delta to x and y
				nx, ny = x + dx, y + dy
				if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
					grid[nx][ny] = "0"
					queue.append((nx, ny))

	def numIslands(self, grid: list[list[str]]) -> int:
		m = len(grid)
		n = len(grid[0])
		island_count = 0

		for i in range(m):
			for j in range(n):
				if grid[i][j] == "1":
					self.__bfs(i, j, grid)
					island_count += 1
		return island_count

# Time Complexity: Explores all the nodes only once, so O(n*m)
# Space complexity: Queue can grow as big as all the nodes, so also O(n*M)