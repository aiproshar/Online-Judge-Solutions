'''
Default Brute Force Approach
TLE, no way this is passable
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            total = nums[i]
            for j in range(i+1,len(nums)):
                total += nums[j]
                if total % k == 0:
                    return True
        return False

# Time Complexity: O(n^2)
# Space Complexity: O(1)



'''
FK this problem, more feels like Number theory than data structure and algorithms

The math is straight forward, but we have two edge cases

modK == 0, imagine our first element and second element both divisible by K, initially we put 0:0 then 1->0
It does not satisfy min len constrain, so we prime index -1 as 0, so if we find reminder 0 in first index, we skip due
to len consrain and when we find again in second index, wala we have a match
'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        # The most important corner case, populating the mod 0 value
        # Took hours to understand
        prev = {0: -1}
        prev_sum = 0

        for i in range(len(nums)):
            prefix_sum[i] = prev_sum + nums[i]
            prev_sum = prefix_sum[i]
            if prefix_sum[i] % k in prev:
                if i - prev[prefix_sum[i] % k] > 1:
                    return True
            else:
                prev[prefix_sum[i] % k] = i
        return False

# Time Complexity: O(n)
# Space Complexity: O(n) for prefix sum and lookup table
