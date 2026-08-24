
'''
Word Search I based solution, same code
TLE as expected, no trie on ly backtrack and DFS
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i, x, y, word, board):
            if i == len(word):
                return True
            direction = [
                [0, 1],
                [-1, 0],
                [1, 0],
                [0, -1]
            ]
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == word[i]:
                        board[nx][ny] = None
                        if backtrack(i + 1, nx, ny, word, board):
                            board[nx][ny] = word[i]
                            return True
                        board[nx][ny] = word[i]
            return False

        res = set()
        for word in words:
            for i in range(len(board)):
                # speedup, if we already got a match lets skip
                if word in res:
                    break
                for j in range(len(board[0])):
                    # speedup, if we already got a match lets skip
                    if word in res:
                        break
                    if board[i][j] == word[0]:
                        board[i][j] = None
                        if backtrack(1, i, j, word, board):
                            res.add(word)
                        board[i][j] = word[0]
        return list(res)
# Time Complexity: 3^l * m * n * w (l = length of each word, w = no of words)
# space: O(l) recursion depth
# This gets TLE