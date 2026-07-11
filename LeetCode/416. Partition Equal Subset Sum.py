class Solution:
    class Solution:
        def canPartition(self, nums: List[int]) -> bool:

            total = sum(nums)
            if total % 2 != 0 or len(nums) == 1:
                return False

            target = total // 2

            @cache
            def dp(pos, current_sum) -> bool:

                if current_sum == target:
                    return True
                if current_sum > target or pos == len(nums):
                    return False
                res = []
                # take it
                res.append(dp(pos + 1, current_sum + nums[pos]))
                # Skip it
                res.append(dp(pos + 1, current_sum))
                return any(res)

            return dp(0, 0)


# Time Complexity: O(n * target) 2D dp table -> From 2^N because of memoization
# Space Complexity: len(nums) * sum(nums) oka n*target , we are getting memory limit error




class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0 or len(nums) == 1:
            return False
        target = total // 2
        subset = set()
        def dfs(pos):
            if target in subset or pos == len(nums):
                return
            for item in subset.copy():
                if item + nums[pos] <= target:
                    subset.add(item + nums[pos])
            if nums[pos] <= target:
                subset.add(nums[pos])
            dfs(pos + 1)
        dfs(0)
        if target in subset:
            return True
        else:
            return False
# Time Complexity: O(n * target)
# Space Complexity: O(target) upper bound

'''
True DP solution
dp[num] -> Can we reach num ? and num can range from o to subset_sum
Backward to avoid double counting (eqv of copy of previous solution)
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0 or len(nums) == 1:
            return False
        subset_sum = total // 2
        dp = [False] * (subset_sum + 1)
        dp[0] = True
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[subset_sum]

# S -> sum(nums)
# Time Complexity: O(S * n)
# Space Complexity: O(S)