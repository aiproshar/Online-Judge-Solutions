'''
My Fav Top Down recursive DP
'''


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # Maximize T, Maximize F
        # Return the largest continious block
        @cache
        def dp(i: int, prev: int, flip: int, candidate: str) -> int:

            if i == len(answerKey):
                return prev

            if answerKey[i] == candidate:
                return dp(i + 1, prev + 1, flip, candidate)
            else:
                # We need to flip, can we flip ?
                res = []
                if flip > 0:
                    # flip
                    res.append(dp(i + 1, prev + 1, flip - 1, candidate))
                # dont flip (doesnt matter if its intentional or not)
                '''
                This is an edge case, we we are doing a reset, we must store our current
                streak of similar count before pressing reset
                That's why push: res.append(prev)
                '''
                res.append(prev)
                res.append(dp(i + 1, 0, flip, candidate))
                return max(res)

        return max(
            dp(0, 0, k, "T"),
            dp(0, 0, k, "F")
        )

# Time Complexity: O(n^2 * k)
# Space Complexity: O(n^2 * k)
# MLE due to @cache