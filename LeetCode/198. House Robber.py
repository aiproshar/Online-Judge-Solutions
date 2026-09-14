class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. Objective Function dp(x) -> from 0 to X house, our max money
        # dp(1) -> max money from 0, 1 index houses
        # dp(5) -> max money from 0,1,..5 index houses
        @cache
        def dp(n) -> int:
            # 2. Base Cases
            if n == 0:
                # only one choice so rob it what it can take
                return nums[0]

            if n == 1:
                # We have two choices, 0th or 1st house
                # Take the best one no consequences
                return max(nums[0], nums[1])

            # 3. Recurrence Relation
            # We rob current house or we leave it
            # Rob it or Skip it
            # Optimization problem
            return max(nums[n] + dp(n - 2), dp(n - 1))

        # 4: Order of Computation: Top Down
        # 5: Result: whatever objective function retuns. We need index of houses from 0 to ith.
        # To include all houses its len(nums) - 1
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
# Followup -? can you do this in constant space ?


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        pre_second = nums[0]
        pre_first = max(nums[0], nums[1])

        for i in range(2, n):
            temp = max(nums[i] + pre_second, pre_first)
            pre_first, pre_second = temp, pre_first

        return pre_first

# Time Complexity: O(n)
# Space: O(1)
