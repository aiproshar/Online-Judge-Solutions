'''
Top Down recursive + Memoization
Deduction on initial problem so we can build the objective function

The idea is after all the stone merge, in the end its the sum of all the stones, where some weights are negated
So for each weight we have 2 choices, positive or negative
The optimization is we want negative to add upto close to half or equal half
Use Gemini for more in depth explore
'''
class Solution:

    def lastStoneWeightII(self, stones: list[int]) -> int:

        target = sum(stones) // 2

        @cache
        def dp(i, current) -> int:
            # Corner Case, if you
            if current < 0:
                return math.inf
            if i == len(stones):
                return current
            if current == 0:
                return 0

            res = [
                dp(i + 1, current),
                dp(i + 1, current - stones[i])
            ]
            return min(res)

        leftover = dp(0, target)
        print(leftover)
        target -= leftover
        return sum(stones) - (2 * target)

# Time Complexity: O(n * S), where S is sum(stones)
# Space Complexity: O(n)