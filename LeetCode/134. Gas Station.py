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

'''
Tried this again and was able to solve, was stuck for 10 minutes
This is actually kadanes lol
If current is negative we start from there
'''
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        gain = [gas[i] - cost[i] for i in range(n)]
        idx = 0
        current = 0
        for i in range(n):
            if gain[i] > current + gain[i]:
                # reset
                current = gain[i]
                idx = i
            else:
                # extend
                current += gain[i]
        return idx
