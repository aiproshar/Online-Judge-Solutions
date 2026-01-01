
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


# Follow UP 
# Doing in constant space
# We only need to save the previous state

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prev_min = nums[0]
        prev_max = nums[0]
        mx = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                # Python magic wala ! No need for temp vars
                prev_min, prev_max = min(nums[i], prev_max * nums[i]), max(nums[i], prev_min * nums[i])
            else:
                # YaY
                prev_min, prev_max = min(nums[i], prev_min* nums[i]), max(nums[i], prev_max * nums[i])
            mx = max(mx, prev_max)
        return mx

# Time Complexity: O(n)
# Space complexity: O(1)



        

        