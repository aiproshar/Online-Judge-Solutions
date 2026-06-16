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



# Algorith : Kadane's Algorith for O(n) Solution
# /Brute Force : O(n^2) solution, Returns global optimum
# Kind of DP + Greedy Behavior. Dp stores greedy's local optimum, greedy extends gradually to global space by extending local space
# Back to back SWE explanation : https://www.youtube.com/watch?v=2MmGzdiKR9Y
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        current = 0
        for num in nums:
            if current + num < num:
                current = num
            else:
                current = current + num
            max_sum = max(max_sum, current)
        return max_sum

# Time Complexity: O(n)
# Space Complexity: O(1)