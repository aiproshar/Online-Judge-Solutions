"""
One Liner, to make interviewer angry

"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


'''
Typical simulation, Linear
keep multiplying x , this also gets TLE
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        ans = 1
        for i in range(abs(n)):
            ans *= x
        if n < 0:
            ans = 1.00 / ans
        return ans
# Time Complexity: linear

"""
Recursion, but no branch out
to calculate x^10, we need x^5 and multiply to x^5
To calculate x^5, we do same for x^4 which is even and multiply x
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1.0 / x
            n = -1 * n

        def recurse(x, n) -> int:
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2 == 0:
                ans = recurse(x, n // 2)
                ans = ans * ans
                return ans
            else:
                ans = recurse(x, n // 2)
                ans = ans * ans * x
                return ans

        return recurse(x, n)


# Time Complexity: log(n)
