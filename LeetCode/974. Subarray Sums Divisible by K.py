class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # key: remainder -> number of index where prefix_sum % k == remainder
        rem_to_count = defaultdict(int)
        # the whole array
        rem_to_count[0] = 1
        n = len(nums)
        current = 0
        ans = 0
        for i in range(n):
            current += nums[i]
            remainder = current % k
            ans += rem_to_count[remainder]
            rem_to_count[remainder] += 1
        return ans

# Time Complexity: O(n)
# Space Complexity: O(min(n, k))