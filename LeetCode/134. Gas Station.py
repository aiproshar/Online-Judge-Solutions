'''
Brute Force Solution
We start from each station and try to do a full loop
TLE
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            tank = gas[start]
            idx = start
            total = 0
            # Not running out of gas
            while tank - cost[idx] >= 0:
                total += 1
                tank -= cost[idx]
                idx = (idx + 1) % n
                tank += gas[idx]
                # Break the infinite loop if we have a
                if total == n:
                    break
            if total == n:
                return idx
        return -1
# Time Complexity: O(N^2)
# Space: O(1)


'''
Greedy Approach
Weird, Problem specific, bit of math intuition. This problem should not suitable for coding test
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1
        total = 0
        start_idx = 0

        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start_idx = i + 1
        return start_idx