'''
TLE, Brute Force
GO through each number in range and make sure its valid

'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for num in range(low, high + 1):

            num_str = [int(d) for d in str(num)]

            for i in range(len(num_str) - 1):
                if num_str[i + 1] == num_str[i] + 1:
                    continue
                else:
                    break
            else:
                res.append(num)
        return res

# Time Complexity: nlog(10)n  AKA n> digit_count n
# Space Complexity: Recursion Depth, log(10)n


class Solution:
    def to_int(self, digits):
        n = 0
        for d in digits:
            n = n * 10 + d
        return n

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def recurse(state: list):

            if len(state) > 11:
                return
            answer = self.to_int(state)
            if low <= answer <= high:
                res.append(answer)
            for num in range(1, 10):
                if num == state[-1] + 1:
                    state.append(num)
                    recurse(state)

        for i in range(1, 10):
            recurse([i])
# Time and Space: O(1) precompute is bounded by 10^9
