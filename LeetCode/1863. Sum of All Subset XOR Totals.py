'''
Initial Solution, Everything is okay but we have global mutating state
Which is considered a bad practice
'''
class Solution:
    sum_ = 0

    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def backtrack(i, xor):
            nonlocal total
            if i == len(nums):
                total += xor
                return
            # take i
            xor ^= nums[i]
            backtrack(i + 1, xor)
            xor ^= nums[i]
            # skip i
            backtrack(i + 1, xor)
            return

        backtrack(0, 0)

        return total
# Time Complexity: 2^N
# Space: O(n)

# Same solution without global mutating state, pure functions
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(i, xor) -> int:
            if i == len(nums):
                return xor
            sum_ = 0
            # take i
            sum_ += backtrack(i + 1, xor ^ nums[i])
            # skip i
            sum_ += backtrack(i + 1, xor)
            return sum_

        return backtrack(0, 0)
# Time: O(2^n)
# Space: O(n)