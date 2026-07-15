'''
Peal Onion method, Bruteforce TLE
'''
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        min_ops = 0
        while True:
            if sum(target) == 0:
                break
            pos = set()
            for idx,num in enumerate(target):
                if num > 0:
                    pos.add(idx)
                    target[idx] -= 1
            subsets = len(pos)
            for idx in pos:
                if idx+1 in pos:
                    subsets -= 1
            min_ops += subsets
        return min_ops

# Time Complexity: O(n* max(target))
# Space: O(1)


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        ops = [None] * len(target)
        ops[0] = target[0]

        for i in range(1, len(ops)):
            if target[i] <= target[i - 1]:
                # no additional work
                ops[i] = 0
            elif target[i] > target[i - 1]:
                # additional work on that index
                ops[i] = target[i] - target[i - 1]

        return sum(ops)
# Time Complexity: O(n)
# Space: O(n) , can be down to O(1)