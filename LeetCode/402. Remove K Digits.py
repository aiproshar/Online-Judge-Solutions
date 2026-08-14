'''
Basic Monotonic Increasing Stack
Corner Case, we must remove K anyway, and if the input if already perfect,
example 1 2 3 4 5 and k =2, we must pop the LSB to remove 4 and 5
Some formating constraint and we good
'''
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:

        stack = []
        nums = [int(x) for x in s]

        for  num in nums:
            # Monotonically increasing stack
            # newer smaller values violates property, so restore
            while stack and num < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num)
        while stack and k > 0:
            stack.pop()
            k -= 1
        stack = [str(x) for x in stack]
        res = "".join(stack).lstrip('0')
        if res == "":
            return "0"
        return res
# Time Complexity: O(n)
# Space Complexity: O(n)
