class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sources = []
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                sources.append((0, j))
            if board[len(board) - 1][j] == 'O':
                sources.append((len(board) - 1, j))

        for i in range(len(board)):
            if board[i][0] == 'O':
                sources.append((i, 0))
            if board[i][len(board[0]) - 1] == 'O':
                sources.append((i, len(board[0]) - 1))

        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        visited = set()
        que = deque()
        for source in sources:
            visited.add(source)
            que.append(source)
        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == 'O' and (nx, ny) not in visited:
                        que.append((nx, ny))
                        visited.add((nx, ny))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'

# Time Complexity: O(m*n)
# space complexity: O(m*n)



'''
In place modification, no extra visited set needed
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sources = []
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                sources.append((0, j))
            if board[len(board) - 1][j] == 'O':
                sources.append((len(board) - 1, j))

        for i in range(len(board)):
            if board[i][0] == 'O':
                sources.append((i, 0))
            if board[i][len(board[0]) - 1] == 'O':
                sources.append((i, len(board[0]) - 1))

        direction = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        que = deque()
        for source in sources:
            que.append(source)
            board[source[0]][source[1]] = '#'
        while que:
            x, y = que.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == 'O':
                        que.append((nx, ny))
                        board[nx][ny] = '#'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

# Time Complexity: O(m*n)
# Space Complexity: O(m+n) -> Why ?
# --------------------------------------------------------------------
        # STEP 2: The BFS Queue (The Wavefront)
        # --------------------------------------------------------------------
        # Why doesn't the queue size reach O(M * N)?
        # Because BFS processes grids like a expanding ripple/wave. At any single
        # moment, the queue ONLY holds the current "frontier" line, not the
        # whole history of visited cells.
        #
        # Visualizing the BFS Queue shrinking inward:
        #
        # T = 0 (Initial Queue elements '#')     T = 1 (Next layer expanding inward)
        #   #  #  #  #  #                          O  O  O  O  O
        #   #  .  .  .  #                          O  #  #  #  O
        #   #  .  .  .  #                          O  #  .  #  O
        #   #  .  .  .  #                          O  #  #  #  O
        #   #  #  #  #  #                          O  O  O  O  O
        # Queue Size = Perimeter = O(M + N)      Queue Size = Inner Perimeter < O(M + N)
        # --------------------------------------------------------------------