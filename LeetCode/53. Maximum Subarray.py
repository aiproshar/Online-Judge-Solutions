'''
Bruteforce  TLE
ALl possible subarray and compare with global Max
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(current_sum, max_sum)
        return max_sum
# Time Complexity: O(n^2) TLE
# Space COmplexity: O(1)

'''
Raws Kadane, extend or start fresh !
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = nums[0]

        for i in range(1, len(nums)):
            # continue expand or start fresh, kadanes algorithm
            current = max(current + nums[i], nums[i])
            max_sum = max(max_sum, current)

        return max_sum

# Time Complexity: O(n)
# Space: O(1)