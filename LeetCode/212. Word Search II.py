
'''
Word Search I based solution, same code
TLE as expected, no trie only backtrack and DFS
'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(x, y, idx, word) -> bool:
            # Check For Goals
            if idx == len(word):
                return True
            # Constrains
            if (
                    x < 0
                    or y < 0
                    or x >= len(board)
                    or y >= len(board[0])
                    or board[x][y] != word[idx]
            ):
                return False

            # Choices + backtrack
            board[x][y] = '#'
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if backtrack(nx, ny, idx + 1, word):
                    # backtrack
                    board[x][y] = word[idx]
                    return True
            # backtrack
            board[x][y] = word[idx]
            return False

        res = set()
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if backtrack(i, j, 0, word):
                        res.add(word)
        return list(res)

# Time Complexity: 3^l * m * n * w (l = length of each word, w = no of words)
# space: O(l) recursion depth
# This gets TLE


'''
Trie Based Solution with bunch of optimization
Took almost a whole day, 
'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def _add(word: str) -> None:
            current = trie
            for char in word:
                if char not in current:
                    current[char] = {}
                current = current[char]
            # Optimization: Add the word as value in end marker, so we don't need to carry recursion state
            current[None] = word

        for word in words:
            _add(word)
        res = []

        def backtrack(x, y, trie_):
            # Goals
            if None in trie_:
                # Optimization
                # Remove end marker to avoid duplicate
                # We don't need a set to handle duplicates anymore
                res.append(trie_[None])
                del trie_[None]
            # Constrains
            if (
                    x < 0
                    or y < 0
                    or x >= len(board)
                    or y >= len(board[0])
                    or board[x][y] not in trie_
            ):
                return
            temp = board[x][y]
            board[x][y] = '#'
            # Choices + Backtrack
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                backtrack(nx, ny, trie_[temp])
            board[x][y] = temp
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, trie)
        return res
# Time Complexity: W * L for trie buildup, M * N * 3^L
# Space: W * L for trie, and O(L) recursion depth and also anwer W * L