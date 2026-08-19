'''
Simple DFS search, with external for loop to kick off DFS upon first character match
Similar to Graph Problems, but this is more of backtracking
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(x, y, idx, board) -> bool:
            if idx == len(word):
                return True

            direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == word[idx]:
                        temp = board[nx][ny]
                        board[nx][ny] = None
                        res = backtrack(nx, ny, idx + 1, board)
                        board[nx][ny] = temp
                        if res:
                            return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = None
                    if backtrack(i, j, 1, board) is True:
                        board[i][j] = word[0]
                        return True
                    board[i][j] = word[0]
        return False
# Time Complexity: We have 4 choices, but one of them is grandparent, so its 3. so O(3^L) , where L is word length
# We start DFS for M*N times, so M*N*3^L
# Space Complexity: O(L) recursion depth + we do modify the board so O(M*N) discusss with interviewer