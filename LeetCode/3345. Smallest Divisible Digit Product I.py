class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            current = n
            mul = 1
            while current:
                mul = mul * (current % 10)
                current = current // 10
            if mul % t == 0:
                return n
            else:
                n += 1
# Time Complexity: T ranges from 1 <= t <= 10, so we need 10 outer most iteration so remainder matches up
# On each iteration, we do logn work, (10 based log), so this is tlogn [Note: 10 based log, not 2 based]
# Space: Constant