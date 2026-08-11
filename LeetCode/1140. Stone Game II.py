
'''
Game theory min/max dp
With bit of complexity is range, state calculation
Others are almost same
'''
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @cache
        #
        def dp(i, m, turn) ->int:
            if i >= len(piles):
                return 0
            current = 0
            count = 0
            res = []
            for x in range(i, i + 2*m):
                if x >= len(piles):
                    break
                current += piles[x]
                count += 1
                res.append(
                    # initially i wrote only current + dp(...) which was wrong
                    # We are calculating alice's total, so in bobs term we dont
                    # Add current at all, we just take next recursive call
                    # Which is Alices stone
                    # TLDR: when the stones owned by bob skip
                    (current if turn else 0) + dp(x+1, max(count, m),  not turn)
                )
            if turn:
                return max(res)
            else:
                return min(res)
        return dp(0,1,True)
# State Space, Its n*n, M is also bounded by n, and a boolean adds a constant factor of 2
# Time Complexity: n work per state due to loop, n*n state space. so its O(n^3)
# Space Complexity: O(n^2) state, o(n> recursion depth