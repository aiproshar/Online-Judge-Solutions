# Nasty Problem, Reference Judge Check
# So we need to do inplace or use the original array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        u = 1
        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]:
                continue
            else:
                nums[u] = nums[i]
                u += 1
        return u

