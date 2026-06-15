"""
In Place Solution, a lot of edge cases
We must preserve the original zeros and we must not run expansion on non-original zeros

"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        None: Our new zero candidates, will be zero in final pass
        If we make new candidates zero, we will also expand based on them, that will throw wrong answer
        Also we cannot set everything to 0, as we might omit original 0s in the row/column
        This 2 corner case must be kept in mind
        """
        m = len(matrix) # row
        n = len(matrix[0]) # col
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for x in range(m):
                        # Only None if not zero, we make them for zero later
                        matrix[x][j] = 0 if matrix[x][j] == 0 else None
                    for y in range(n):
                        # Only None if not zero, we make them for zero later
                        matrix[i][y] = 0 if matrix[i][y] == 0 else None

        # Final Pass, make new candidates zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        return matrix

# Time Complexity: Every cell, so m*n, on each sell we expand row and col, so m*N(m+n)
# Space Complexity: O(1) no extra space as per problem constraint