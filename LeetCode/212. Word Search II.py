"""
My gorgeous solution using Trie but getting TLE
Sad Life
"""
class Solution:
    def __init__(self):
        self.root = {}
        self.word_list = set()

    def append(self, lst):
        word = "".join(lst)
        if word in self.word_list:
            return
        self.word_list.add(word)
        curr = self.root
        for w in word:
            if w in curr:
                curr = curr[w]
            else:
                curr[w] = {}
                curr = curr[w]

    def find(self, word):
        curr = self.root
        for w in word:
            if w in curr:
                curr = curr[w]
            else:
                return False
        return True

    def backtrack(self, board, i, j, path):
        deltas = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        path.append(board[i][j])
        board[i][j] = None

        further = False
        for dx, dy in deltas:
            ni = i + dx
            nj = j + dy
            # look before you leap
            if 0 <= ni < len(board):
                if 0 <= nj < len(board[0]):
                    if board[ni][nj] is not None:
                        self.backtrack(board, ni, nj, path)
                        further = True

        if not further:
            self.append(path)
            # Backtrack
        board[i][j] = path.pop()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                self.backtrack(board, i, j, [])
        res = [word for word in words if self.find(word)]
        return res
