
# Recursive backtrack
# Each step we take the number or we dont
# When there is no number to take, we construct the list (via copy) and insert in in list of lists

class Solution(object):
    def traverse(self, current: list, nums: list, idx: int):
        if idx == len(nums):
            self.subsets.append(current[:])
        else:
            current.append(nums[idx])
            self.traverse(current, nums, idx+1)
            current.pop()
            self.traverse(current, nums, idx+1)

    def subsets(self, nums):
        self.subsets = []
        self.traverse([], nums, 0)
        return self.subsets