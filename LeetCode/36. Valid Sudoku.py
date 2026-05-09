"""
Important problem, we learn to solve basic adhoc in pythonic way
Zip -> to column iteration
I was using Counter initially, but it was overkill, i didn't need that granular info
Push everything into list, how we detect duplicate in list  ?
len(list) == len(set(list)) tells us if there is any duplicate
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row_num = [item for item in row if item != "."]
            if len(row_num) != len(set(row_num)):
                return False

        for col in zip(*board):
            col_num = [item for item in col if item != "."]
            if len(col_num) != len(set(col_num)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_elements = []
                for dx in range(0, 3):
                    for dy in range(0, 3):
                        if board[i + dx][j + dy] != ".":
                            box_elements.append(board[i + dx][j + dy])
                if len(box_elements) != len(set(box_elements)):
                    return False
        return True
# time complexity: O(1)
# Space Complexity: O(1) //Our box is always 9*9