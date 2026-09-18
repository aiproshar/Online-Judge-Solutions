class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()

        @cache
        def dp(remain) -> int:
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            ans = 0
            for num in nums:
                if remain - num < 0:
                    break
                ans += dp(remain - num)
            return ans

        return dp(target)

# Time Complexity: O(target * n), and recursion depth of target//min(nums)
# Space: O(target)

'''
Bottom UP with micro optimization

'''

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        for i in range(target+1):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
                else:
                    # micro optimization as if current num is larget all later are larger even more
                    break
        return dp[target]

# Time Complexity: O(target * n)
# Space Complexity: O(target)