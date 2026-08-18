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

'''
Take it or leave it approach
in each step take i or leave it and go to next step
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, sum_, current):
            if sum_ == target:
                res.append(current.copy())
                return
            if i >= len(candidates) or sum_ > target:
                return

            # take i the element
            current.append(candidates[i])
            backtrack(i, sum_ + candidates[i], current)
            current.pop()

            # leave dont take ith element
            backtrack(i + 1, sum_, current)

        backtrack(0, 0, [])
        return res

'''
Most efficient solution, slight variation of 1st solution
Early Termination Logic due to sorting
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(start, sum_, current):
            if sum_ == target:
                res.append(current.copy())
                return
            if sum_ > target:
                return
            for i in range(start, len(candidates)):
                if sum_ + candidates[i] > target:
                    break
                current.append(candidates[i])
                backtrack(i, sum_ + candidates[i], current)
                current.pop()
            return
        backtrack(0, 0, [])
        return res