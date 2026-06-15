"""
Problem: Minimum Moves to Equal Array Elements II

Given an array, make all elements equal using minimum moves.
Each move: increment or decrement one element by 1.

Key Insight: The optimal target is the MEDIAN.

Why? Imagine numbers as points on a number line:
- Pick a target too far right → left numbers travel extra
- Pick a target too far left  → right numbers travel extra
- The median balances both sides, minimizing total distance

Example: [1, 3, 7]
  Target = median = 3
  Cost = |1-3| + |3-3| + |7-3| = 2 + 0 + 4 = 6  ✓
  Target = 4 (not median)
  Cost = |1-4| + |3-4| + |7-4| = 3 + 1 + 3 = 7  ✗ worse

Even-length edge case: [1, 3, 5, 7]
  Two middle values: 3 and 5
  ANY target between them (inclusive) gives the same cost.
  So just picking nums[n//2] always works.

Time:  O(n log n) for sorting
Space: O(1) extra (ignoring sort internals)
"""


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Sort so the median is simply the middle element
        nums.sort()

        # Grab the median (right-of-center for even lengths — works either way)
        median = nums[len(nums) // 2]

        # Sum up how far every element is from the median
        cost = 0
        for i in range(len(nums)):
            cost += abs(nums[i] - median)

        return cost