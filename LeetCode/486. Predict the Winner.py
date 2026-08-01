'''
Beautiful DP problem, 2D state. Min Max swap n+1 step
Initially thought as 3D due to turn (is it player a or b), but later realized it can be deducted from i and j
In player A term is maximization problem, in B it's minimization problem
'''
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        total = sum(nums)
        @cache
        def dp(i ,j) -> int:
            # Our Function returns maximized value for player A
            if i > j:
                return 0
            if (i + (len(nums) - 1 - j)) % 2 == 0:
                # Player 1's term
                left = nums[i] + dp( i +1, j)
                right = nums[j] + dp(i, j- 1)
                return max(left, right)
            else:
                # Player 2's term
                # minimaizing player 1's point
                left = dp(i + 1, j)
                right = dp(i, j - 1)
                return min(left, right)

        first = dp(0, len(nums) - 1)
        if first >= total - first:
            return True
        else:
            return False
# Time Complexity: O(n^2), all possible combination of i,j
# Space Complexity: O(n^2) State Space