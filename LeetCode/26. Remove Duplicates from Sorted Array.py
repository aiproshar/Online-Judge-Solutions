# Nasty Problem, Reference Judge Check
# So we need to do inplace or use the original array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        res = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] == res[-1]:
                continue
            else:
                res.append(nums[i])
        nums.clear()
        for x in res:
            nums.append(x)
