'''
Simple DFS search, with external for loop to kick off DFS upon first character match
Similar to Graph Problems, but this is more of backtracking

Updated solution, most stable template
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(x, y, idx) -> bool:
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

            # Choices
            board[x][y] = None
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if backtrack(nx, ny, idx + 1):
                    # backtrack
                    board[x][y] = word[idx]
                    return True
            # backtrack
            board[x][y] = word[idx]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False

# Time Complexity: We have 4 choices, but one of them is grandparent, so its 3. so O(3^L) , where L is word length
# We start DFS for M*N times, so M*N*3^L
# Space Complexity: O(L) recursion depth + we do modify the board so O(M*N) discusss with interviewer