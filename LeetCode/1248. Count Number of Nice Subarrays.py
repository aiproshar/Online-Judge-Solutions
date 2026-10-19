'''
Not so obvious solution. Seems like a sliding window but actually prefix_sum variant (two pointer)
Harder Two Pointers
'''
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:


        # odds -> prefix_count with keys number of odds
        odds = defaultdict(int)
        odds[0] = 1
        current = 0
        count = 0
        for i in range(len(nums)):

            if nums[i] % 2 != 0:
                current += 1
            if current >= k:
                required_deduct = current - k
                count += odds[required_deduct]
            odds[current] += 1

        return count

# Time Complexity: O(n)
# Space Complexity: O(n)