'''
Generic Solution, works for any of them
'''
class Solution:

    def assemble(self, nums: list[int], skip_: set, current: int):
        i = 0
        j = 0
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] in skip_:
                continue
            else:
                j = max(j, i + 1)
                while j < n and nums[j] != current:
                    j += 1
                if j == n:
                    # no more current left
                    break
                else:
                    nums[i], nums[j] = nums[j], nums[i]

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.assemble(nums, {0}, 0)
        self.assemble(nums, {0, 1}, 1)
        return nums

# Time and Space complexity: O(n)