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

'''
Actually this is a sliding window problem
This is similar to : https://leetcode.com/problems/longest-repeating-character-replacement/description/

Slide and Get global optimization
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        # Maximize T, Maximize F
        # Return the largest continious block

        def sliding(char: str) -> int:
            mismatch = 0
            max_len = 0
            left = right = 0
            for right in range(len(answerKey)):

                # slide right
                if answerKey[right] != char:
                    mismatch += 1

                # invalid state, shrink
                while mismatch > k:
                    if answerKey[left] != char:
                        mismatch -= 1
                    left += 1
                # valid state, calulate desired property (save global max/min whatever)
                max_len = max(max_len, right - left + 1)
            return max_len

        return max(
            sliding('T'),
            sliding('F')
        )

# Time Complexity: O(n)
# Space Complexity: O(1)