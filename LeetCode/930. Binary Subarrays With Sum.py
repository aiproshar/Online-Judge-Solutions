class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        current = 0
        total = 0

        for i in range(len(nums)):
            current += nums[i]

            if current >= goal:
                target = current - goal
                total += prefix_sum[target]

            prefix_sum[current] += 1

        return total

# Time Complexity: O(n)
# Space Complexity: O(n)the
