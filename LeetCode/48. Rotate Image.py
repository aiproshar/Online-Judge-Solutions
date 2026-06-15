"""
Avoiding constraints, we're using extra memory
Python ZIP to improve QoL
Each row becomes column and revered
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        cols = zip(*matrix)
        for col in cols:
            lst = list(col)
            lst.reverse()
            res.append(lst)
        for i in range(len(matrix)):
            matrix[i] = res[i]

# Time and Space Complexity: O(n*n)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # swap row/col
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                # Early termination optimization, Complexity remains same
                # We are going through lower diag
                if j < i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                else:
                    break
        # Reverse
        for row in matrix:
            row.reverse()
# Time Complexity: O(n*n)
# Space Complexity: O(1)
