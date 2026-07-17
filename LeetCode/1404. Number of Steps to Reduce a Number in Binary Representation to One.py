
'''
Kind of Bruteforce approach
'''
class Solution:
    def numSteps(self, s: str) -> int:

        num = 0
        exponent = 0
        for digit in reversed(range(len(s))):
            num += 2 ** exponent * int(s[digit])
            exponent += 1

        steps = 0

        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num + 1
            steps += 1
        return steps

# Time Complexity: O(n) but for bit level operations, O(n^2)
# Space: O(1)



