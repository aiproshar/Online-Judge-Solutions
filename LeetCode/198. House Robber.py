# Recursive top down solution
# Every state is all the houses upto that one
# We have two choices, we rob current house or skip it and use the previous upto house value
# Took quite a while to find the recurrence relation
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [None for _ in range(len(nums))]

        dp[0] = nums[0]

        def maxMoney(idx: int):
            if idx < 0:
                return 0
            if idx == 0:
                return dp[0]
            if dp[idx] != None:
                return dp[idx]
            # Most tricky part, finding out the recurrence relation
            dp[idx] = max(maxMoney(idx - 2) + nums[idx], maxMoney(idx - 1))
            return dp[idx]
        
        maxMoney(len(nums) - 1)
        
        return dp[-1]

# Time complexity: O(n)
# space complexity: O(n)

# Bottom up iterative
# Initially calculate the two values (bound check also) so we dont get negative index
# Bound check bound check handle initial corner case

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0] if len(nums) == 1 else max(nums[0], nums[1])
        
        dp = [None for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[len(nums) - 1]

# Time and space complexity: O(n)
# Followup -? can yoiu do this in constant space ?
