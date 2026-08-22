

'''
Subset Based Solution, gets TLE
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        sum_ = sum(matchsticks)
        if sum_ % 4 != 0:
            return False
        partial = sum_ // 4
        n = len(matchsticks)
        taken = set()
        # Non increasing sorting
        matchsticks.sort(reverse=True)
        if matchsticks[0] > partial:
            return False

        def backtrack(count, current):
            if current == partial and count == 3:
                return True
            if current == partial:
                current = 0
                count += 1
            for i in range(n):
                if i in taken:
                    continue
                if current + matchsticks[i] > partial:
                    continue
                taken.add(i)
                if backtrack(count, current + matchsticks[i]) is True:
                    return True
                taken.remove(i)
            return False

        return backtrack(0, 0)

# Time Complexity: O(n!)
# Space Complexity:
'''
This problem was really difficult, i got beaten like dogs
Initial solution was okay, i did a lot of optimization too, but still TLE

WE need to change perspective here, insted of creating permutation and tyting to match side,
What if we go through each and try to add them each side, also we do early pruning if they overgrows
Also we start from the largest to smallest so most amount of early prunning happens
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        sum_ = sum(matchsticks)
        if sum_ % 4 != 0:
            return False
        partial = sum_ // 4
        n = len(matchsticks)
        matchsticks.sort(reverse=True)

        def backtrack(idx, current):

            if idx == n and sum(current) == sum_:
                return True

            for side in range(4):
                if current[side] + matchsticks[idx] <= partial:
                    current[side] += matchsticks[idx]
                    if backtrack(idx + 1, current) is True:
                        return True
                    current[side] -= matchsticks[idx]
            return False
        return backtrack(0, [0,0,0,0])

# Time Complexity: 4 choices each depth, we can go to n depth, so 4^N. But a lot of early pruning
# Space Complexity: O(N) recursion depth