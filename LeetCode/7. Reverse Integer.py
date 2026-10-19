'''
Dont know how this is medium, should be an easy
Just inverse, oh take care of negative separately
'''
class Solution:
    def reverse(self, x: int) -> int:

        range = [
            -1 * (2 ** 31),
            ((2 ** 31) - 1)
        ]
        neg = False
        if x < 0:
            x = -x
            neg = True
        x = int(str(x)[::-1])
        if neg:
            x = -x
        if range[0] <= x <= range[1]:
            return x
        else:
            return 0
# Time Complexity: O(logx)
# Space: O(1)


'''
This is the ideal pop and divide implementation
Remember, only one number in negative that we cannot make positive -2^31, because positive of its if causes overflow
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x == -2 ** 31:
            return 0
        neg = False
        if x < 0:
            x = -x
            neg = True
        rev = 0
        while x != 0:
            if rev * 10 + x % 10 > (2 ** 31) - 1:
                return 0
            rev = rev * 10 + x % 10
            x = x // 10
        if neg:
            rev = - rev
        return rev
