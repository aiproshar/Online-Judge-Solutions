'''
 Cyclic Sort Based Problem

'''
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:

        i = 0
        res = set()
        while i < len(nums):
            # We are at desired position, no need to check
            j = nums[i] - 1
            if i == j:
                i += 1
                continue
            else:
                # The destined place for nums[i]
                if nums[j] == nums[i]:
                    res.add(nums[i])
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
        return list(res)

# Time Complexity: O(n)
# Space Complexity: O(1)