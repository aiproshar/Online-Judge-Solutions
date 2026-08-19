
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

'''
Did this while doing second pass
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(open, close, current):
            if open == n and close == n:
                res.append("".join(current))
                return
            if close > open or open > n or close > n:
                return
            current.append('(')
            backtrack(open + 1, close, current)
            current.pop()

            current.append(')')
            backtrack(open, close + 1, current)
            current.pop()
            return
        backtrack(0, 0, [])
        return res

# Time Complexity: 2^2n * n -> 4^n * n (n constant copy overhead)
# Space Complexity: O(2n) recursion depth, output array size 4^n * n