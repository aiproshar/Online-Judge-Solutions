'''
Top Down Recursive DP, Basic Game theory
'''
class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:

        total = sum(stoneValue)

        @cache
        def dp(i: int, turn: bool) -> int:
            if i >= len(stoneValue):
                return 0
            res = []
            current = 0
            for k in range(i, i + 3):
                if k >= len(stoneValue):
                    break
                if turn:
                    current += stoneValue[k]
                    res.append(dp(k + 1, not turn) + current)
                else:
                    res.append(dp(k + 1, not turn))
            if turn:
                return max(res)
            else:
                return min(res)

        alice = dp(0, True)
        if alice == total - alice:
            return "Tie"
        elif alice > total - alice:
            return "Alice"
        else:
            return "Bob"

# Time Complexity: n states, constant work on each stare. so its O(n)
# Space Complexity: O(n), 2x constant factor overhead