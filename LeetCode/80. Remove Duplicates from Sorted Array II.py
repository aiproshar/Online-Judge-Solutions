'''
General Purpose Implementation
'''
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # How many dupes allowed
        k = 2
        # mark the dupes on one pass
        duplicates = 0
        # First Pass, mark the duplicates, the K value takes effect here
        for i in range(k, len(nums)):
            if nums[i - k] == nums[i]:
                nums[i - k] = None
                duplicates += 1

        # Two pointer, slow first
        # Slow -> iterate over every number
        # Fast: Find the number that's needed to replace a None marked index
        j = 0
        for i in range(len(nums)):
            if nums[i] == None:
                j = max(i + 1, j)
                while j < len(nums):
                    if nums[j] != None:
                        nums[i], nums[j] = nums[j], nums[i]
                        j += 1
                        break
                    else:
                        j += 1
                if j == len(nums):
                    break
        return len(nums) - duplicates

# Time Complexity: O(n)
# Space Complexity: O(1)


