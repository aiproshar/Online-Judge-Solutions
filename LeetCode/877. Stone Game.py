'''
Solved it in a restaurant while eating ramen YaY
I am pretty sure i solved something similar like this
DP minimization maximization optimization problem
'''


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        total = sum(piles)
        n = len(piles)

        @cache
        def dp(start, end) -> int:
            if start > end:
                return 0

            res = [
                dp(start + 1, end) + piles[start],
                dp(start, end - 1) + piles[end]
            ]
            # Is it alices term or bobs
            # How much we already consumed, if we consumed even stones this goes to Alice
            # Else bob
            if (start + end - n + 1) % 2 == 0:
                return max(res)
            else:
                return min(res)

        alice = dp(0, n - 1)

        if alice > total - alice:
            return True
        else:
            return False
# Time Complexity: State Space, O(n^2)
# Space: State Space O(n^2) + recursion depth O(n)


'''
According to game theory, Alice always wins
How ? Alice can choose all even or odd place stones, and bobs choice has no effect
If all even > odd, start with even
If all odd > even, start with odd
How ? If he takes the first one, its guranteed he can take the third, fifth, seventh......
If he takes the last one, its guranteed he can take 2nd, 4th, 6th,......
How ? Do simulation. 
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Fucking Joke, Game Theory
        return True

# Time and Space Complexity: O(1)



