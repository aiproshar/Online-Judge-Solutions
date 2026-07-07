# Recursive top down solution
# Every state is all the houses upto that one
# We have two choices, we rob current house or skip it and use the previous upto house value
# Took quite a while to find the recurrence relation
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i) -> int:
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            rob = nums[i] + dp(i - 2)
            skip = dp(i - 1)
            return max(rob, skip)

        return dp(len(nums) - 1)


# Time complexity: O(n)
# space complexity: O(n)

# Bottom up iterative
# Initially calculate the two values (bound check also) so we dont get negative index
# Bound check bound check handle initial corner case

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [None] * len(nums)
        # Base Cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # Build UP
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]) # Recurrence Relation Eqv
        return dp[-1]

# Time and space complexity: O(n)
# Followup -? can yoiu do this in constant space ?
