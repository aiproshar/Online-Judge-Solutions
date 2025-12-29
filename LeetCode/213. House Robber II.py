# Almost same as House Robber

'''
Thought Process

My initial thought  was we can either have the first one or the last one, and we dont have any other choice
So lets break down the problem into two problems, excluding first one and excluding the last one
Also there was a corner case, where we have only one item, in that case i handled with hard code


'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        # This our corner case
        # For single element, both first set split and last set will be empty []
        # So we wwrongfully return 0
        if len(nums) == 1:
            return nums[0]
        first_set = nums[1:]
        second_set = nums[:-1]


        def rob_subset(nums) -> int:
            n = len(nums)
            if n == 0:
                return 0
            dp = [None for _ in range(n)]
            if n == 1:
                dp[0] = nums[0]
            elif n > 1:
                dp[0] = nums[0]
                dp[1] = max(nums[1], nums[0])
            
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[n - 1]
        
        # Breaking the dp corner case in two sets, and picking the global max
        max_money = max(rob_subset(first_set), rob_subset(second_set))
        return max_money 
        
        # Time: O(n)
        # Space: O(n)