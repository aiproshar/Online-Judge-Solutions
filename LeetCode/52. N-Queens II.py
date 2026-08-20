'''
99% similar as n Queens and easier
We only need the count of solutions, not the board itself
Get rid of board, our collision avoidance s guranteed by the row, cols,digs set

'''


class Solution:
    def totalNQueens(self, n: int) ->int:
        res = 0
        cols = set()
        # negative slope diagonal means row/col moves opposite dir, their sum constant
        n_dig = set()
        # positive slope diagonal means row/col moves same dir, diff remains constant
        p_dig = set()

        def backtrack(row):
            # We already got n queens
            nonlocal res
            if row == n:
                res += 1
                return

            for col in range(n):
                if col in cols or (row + col) in n_dig or (row - col) in p_dig:
                    continue
                else:
                    cols.add(col)
                    n_dig.add(row + col)
                    p_dig.add(row - col)

                    backtrack(row + 1)

                    p_dig.remove(row - col)
                    n_dig.remove(row + col)
                    cols.remove(col)

        backtrack(0)
        return res
# Time Complexity: O(n!), also n check but due to severe running we can put this as n!
# Space Complexity: O(n)