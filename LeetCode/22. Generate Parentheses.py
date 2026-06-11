"""
CCG pattern
Choice on each step: i can take an open or a close
Constrain: We have limited number on each parenthesis type
Goal: Find Valid ones
"""

class Solution:
    def _isValid(self, s: str) -> bool:

        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(open=n, close=n, current=[]):

            if not open and not close:
                if self._isValid(current):
                    res.append("".join(current))
            if open > 0:
                current.append('(')
                open -= 1
                backtrack(open, close, current)
                current.pop()
                open += 1
            if close > 0:
                current.append(')')
                close -= 1
                backtrack(open, close, current)
                current.pop()
                close += 1

        backtrack()
        return res

'''
The time complexity is super difficult in this problem, a lot of crazy math involved, i mean PhD level math FFS
Just use this upper bound, which is way way upper than IRL
'''
# Time Complexity: 2^2n * n -> n*4^n
# Space Complexity: O(n) -> Recursion Depth
# Output array size: n * 4^n (leaf * size in each leaf)





'''
More Clean Implementation
Actually we dont need a valid check at all
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(open_used = 0, close_used = 0, current = []):
            if len(current) == 2*n:
                res.append("".join(current))
                return
            if open_used < n:
                current.append('(')
                backtrack(open_used + 1, close_used, current)
                current.pop()
            if close_used < open_used:
                current.append(')')
                backtrack(open_used, close_used + 1, current)
                current.pop()
        backtrack()
        return res
# Time Complexity: 2^2n * n -> n*4^n
# Space Complexity: O(n) -> Recursion Depth
# Output array size: n * 4^n