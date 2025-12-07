# dfs in 2D grid
# Bound Check and also check we dont get back to previously visited cells
# Also starting point can be any cell, so we need to start dfs from every possible cell
# YaY

class Solution:

    def _dfs(self, row, col, idx) -> bool:
        if idx == len(self.word):
            return True

        if row not in range(len(self.board)) or col not in range(len(self.board[0])):
            return False

        if self.board[row][col] != self.word[idx]:
            return False

        self.board[row][col] = None
        # We can do early termination here upon finding a single true
        explore = [
                self._dfs(row + 1, col, idx + 1),
                self._dfs(row - 1, col, idx + 1),
                self._dfs(row, col + 1, idx + 1),
                self._dfs(row, col - 1, idx + 1),
            ]
        self.board[row][col] = self.word[idx]
        return any(explore)

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word


        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._dfs(i,j,0) == True:
                    return True

        return False

# Time Complexity: brach^depth -> 4^L and we start from all cells, all operations inside a node is constant time, so M*N*1 , O(M*N * 4 ^ L)
# Space complexity: O(L) -> call stack linear space complexity