
# Modified kadane's algorithm
# We need to keep two states, upto min and upto max, thats the corner case
# is current number is negative, multiplying with min so we get max and v.v

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)

        dp_max = [None for _ in range(n)]
        dp_min = [None for _ in range(n)]

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        mx = dp_max[0]

        for i in range(1, n):
            if nums[i] < 0:
                dp_max[i] = max(nums[i], nums[i] * dp_min[i - 1])
                dp_min[i] = min(nums[i], nums[i] * dp_max[i - 1])
            else:
                dp_max[i] = max(nums[i], nums[i] * dp_max[i - 1])
                dp_min[i] = min(nums[i], nums[i] * dp_min[i - 1])
            mx = max(mx, dp_max[i])
        return mx


# Time and space complexity: O(n)



class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        mx_pos = nums[0]
        mx_neg = nums[0]
        global_mx = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mx_pos, mx_neg = mx_neg, mx_pos
            mx_pos = max(mx_pos * nums[i], nums[i])
            mx_neg = min(mx_neg * nums[i], nums[i])
            global_mx = max(global_mx, mx_pos)
        return global_mx


# Time Complexity: O(n)
# Space complexity: O(1)
# Variation of Kadane's Algo
