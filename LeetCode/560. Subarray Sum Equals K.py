
'''
It's a easy problem, but it's not due to negative numbers
Brute force is easy, all possible subarray and compare
'''

# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            _sum = 0
            for j in range(i, len(nums)):
                _sum += nums[j]
                if _sum == k:
                    count += 1
        return count

# Time Complexity: O(n^2)
# Space O(1)

'''
Optimal solution, prefix SUM with hashtable
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)
        # corner case: what if prefix includes all from zero position. Then its valid
        # We assume the array ran past 0 (-1) index, and addition invariant (0)
        prefix_sum[0] += 1
        n = len(nums)
        current = 0
        count = 0
        # inclusive prefix
        for i in range(n):
            current += nums[i]
            target = current - k
            count += prefix_sum[target]
            prefix_sum[current] += 1
        return count

# Time Complexity: O(n)
# Space Complexity: O(1)