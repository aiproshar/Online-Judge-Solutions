# Similar to pacific atlantic flow
# Reverese way BFS

class Solution:
    def __bfs(self, i, j, board: list[list[str]]) -> None:
        if board[i][j] == "X":
            return
        que = deque()
        que.append((i, j))
        self.safe.add((i, j))
        direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "O" and (nx, ny) not in self.safe:
                        self.safe.add((nx, ny))
                        que.append((nx, ny))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.safe = set()

        for j in range(len(board[0])):
            self.__bfs(0, j, board)
            self.__bfs(len(board) - 1, j, board)
        for i in range(len(board)):
            self.__bfs(i, 0, board)
            self.__bfs(i, len(board[0]) - 1, board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in self.safe:
                    board[i][j] = "X"
# Time Complexity: O(m*n), because we only explore the whole grid once
# Space complexity: O(m*n)