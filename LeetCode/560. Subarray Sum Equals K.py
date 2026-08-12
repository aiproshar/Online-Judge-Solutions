
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

        idxs = defaultdict(int)
        idxs[0] = 1
        sum_ = 0
        total = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            total += idxs[sum_ - k]
            idxs[sum_] += 1
        return total
# Time Complexity: O(n)
# Space Complexity: O(n)