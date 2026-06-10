"""
Calculating time and space complexity is the most important part here,
a bit difficult
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx = 0, total = 0, current = []):
            if total == target:
                res.append(current.copy())
                return
            if total > target:
                return
            for i in range(idx, len(candidates)):
                total += candidates[i]
                current.append(candidates[i])
                backtrack(i, total, current)
                current.pop()
                total -= candidates[i]
        backtrack()
        return res
    # Time Complexity: O(n^target) # Choices ^ Depth, each step we have n choices, n = len(candidates)
    # We can go target/min, min can be 1 so lets say depth can go upto target theoretically
    # Space: O(target)
    # Size of output array: n^target * avg size, upper bounded by target