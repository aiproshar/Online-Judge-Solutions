# bruteforce, all possible combinations iteration
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Time complexity: O(n^2)
# Space complexity: O(1)


# Better implementation
# Instead of creating the whole dict, which will have issue in event of duplicate number actually in the list
# we check on the fly. If mirror no there, insert it, Might have mirror in future
# [3,3] works fine now
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            mirror = target - num
            if mirror in nums_dict:
                return [idx, nums_dict[mirror]]
            else:
                nums_dict[num] = idx
        return []


# time complexity: O(n)
# Space Complexity: O(n)

# Another implementation
# Although its nlogn
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums = [(nums[x], x) for x in range(len(nums))]
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[i][0] + nums[j][0] == target:
                return [nums[i][1], nums[j][1]]

            elif nums[i][0] + nums[j][0] > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]