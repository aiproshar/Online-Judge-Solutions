# Kinda shortcut solution
# Instead of all these on the fly 1d <-> 2d translation, we just converted them to a 1D array and ran bi-search there

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nums = [num for row in matrix for num in row]

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
# Time complexity: O(lgN)
# Space Complexity: O(n)




class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def index_val(idx) -> int:
            n = len(matrix[0])
            row = idx // n
            col = idx % n
            return matrix[row][col]

        m = len(matrix)
        n = len(matrix[0])

        lo = 0
        hi = m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == index_val(mid):
                return True
            elif target > index_val(mid):
                lo = mid + 1
            else:
                hi = mid -1
        return False
# Time complexity: O(lg(m*n))
# SPace Complexity: O(1)


