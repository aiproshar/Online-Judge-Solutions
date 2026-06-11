class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        is_match = False
        def backtrack(row, col, i = 0) -> bool:
            # Goals
            if i == len(word):
                return True
            # Constrains
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != word[i]:
                return False
            board[row][col] = None
            explore = [
                # choices
                backtrack(row+1, col, i+1),
                backtrack(row-1, col, i+1),
                backtrack(row, col+1, i+1),
                backtrack(row, col-1, i+1)
            ]
            board[row][col] = word[i]
            return any(explore)
        # All cell can be start point
        for start_row in range(len(board)):
            for start_col in range(len(board[0])):
                if backtrack(start_row, start_col, 0):
                    return True
        return False

'''
Time And Space Complexity is very important: You might think its 4^L but its actually 
3^L, because one of the direction is parent, which we will skip
Time Complexity: M*N*3^L , where L is the length of word

Space Complexity: Recursion  Depth, O(l) 
'''