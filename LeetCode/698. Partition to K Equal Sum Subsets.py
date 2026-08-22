'''
Beautiful Backtracking problem
But this one is T
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            return False
        subset = total // k
        n = len(nums)

        def backtrack(idx: int, partition: list[int]) -> bool:

            if idx == n:
                return sum(partition) == total

            for i in range(k):
                if partition[i] + nums[idx] <= subset:
                    partition[i] += nums[idx]
                    if backtrack(idx + 1, partition):
                        return True
                    partition[i] -= nums[idx]
            return False

        return backtrack(0, [0] * k)

# Time Complexity: K^N
# Space: O(n)

'''
Optimized Solution
Early invalidate and pruning to avoid duplicate explorations
If two buckets have same value, they are interchangeable, we move forward there
Same idea as subset II / Similar
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)
        if total % k != 0:
            # Not possible to divide into K partitions
            return False
        subset = total // k
        n = len(nums)
        nums.sort(reverse=True)
        # largest number larger than partition sum
        if nums[0] > subset:
            return False

        def backtrack(idx: int, partition: list[int]) -> bool:

            if idx == n:
                return True

            for i in range(k):
                # Pruning to avoid duplicate, forward. Same as subset II
                if i > 0 and partition[i - 1] == partition[i]:
                    continue
                if partition[i] + nums[idx] <= subset:
                    partition[i] += nums[idx]
                    if backtrack(idx + 1, partition):
                        return True
                    partition[i] -= nums[idx]
            return False

        return backtrack(0, [0] * k)
# Same as above, but due to pruning, we dont get TLE