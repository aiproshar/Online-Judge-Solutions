'''
Finally, felt super easy like a medium
AM I GETTING GOOD AT THIS HUH ?
Took < 10 minutes YaY
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        res = []
        cols = set()
        # negative slope diagonal means row/col moves opposite dir, their sum constant
        n_dig = set()
        # positive slope diagonal means row/col moves same dir, diff remains constant
        p_dig = set()

        def backtrack(row):
            # We already got n queens, not possible to land hare without placing n queens
            if row == n:
                temp = ["".join(x) for x in board]
                res.append(temp)
                return

            for col in range(n):
                if col in cols or (row + col) in n_dig or (row - col) in p_dig:
                    continue
                else:
                    cols.add(col)
                    n_dig.add(row + col)
                    p_dig.add(row - col)
                    board[row][col] = 'Q'

                    backtrack(row + 1)

                    board[row][col] = '.'
                    p_dig.remove(row - col)
                    n_dig.remove(row + col)
                    cols.remove(col)

        backtrack(0)
        return res
# TIME: O(n!)
#   Tree size: n choices at row 0, ≤n-1 at row 1, ≤n-2 at row 2, ≤n-3 at row 3 ... → Σ n!/(n-k)! ≤ e·n! = O(n!)
#   Per node: n-iteration loop with O(1) set lookups → O(n·n!) strictly
#   Leaves cost O(n²) to join into strings, but S(n) is empirically tiny (92 for n=8),
#   so that term never dominates. Diagonal pruning also cuts the real tree way below n!,
#   but there's no clean closed form for the pruned size → we quote n!.
#
# SPACE: O(n²) auxiliary
#   board: n²  |  cols/n_dig/p_dig: O(n) each  |  recursion depth: O(n)
#   Output res: S(n)·n², excluded by convention.
#   Note: board is droppable — track path=[col_per_row] and build strings only at
#   leaves → O(n) auxiliary, same time bound.