"""
Simple Backtracking using CCG -> Choices Constrains Goals
This is a bit non-standard, only thinking do we take current element or not
Choices is the current index, we take it or we dont
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def traverse(current, idx):
            # Constrains
            if idx == len(nums):
                # Goal
                subsets.append(current.copy())
                return
            # Choices on current state -> We take current or we dont
            current.append(nums[idx])
            traverse(current, idx+1)
            # backtrack
            current.pop()
            traverse(current, idx+1)
        traverse([],0)
        return subsets
    # Time Complexity: O(n*2^n)
    # Space Complexity: O(n*2^n) if we include result, if not then O(n)

'''

More Generic Solution Below
Choices are all elements, bounded by constrains
More generic approach
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(current=[], start=0):
            subsets.append(current.copy())
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(current, i + 1)
                current.pop()
        backtrack()
        return subsets
    # Time Complexity: O(n*2^n)
    # Space Complexity: O(n*2^n) if we include result, if not then O(n)
