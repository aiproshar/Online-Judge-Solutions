# Default Brute force
# Tricky, one zero and no zero edge case handled
# All rest are general case
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_total = 1
        zero_count = 0
        zero_idx = None
        for idx, num in enumerate(nums):
            if num != 0:
                product_total = num * product_total
            else:
                zero_count += 1
                zero_idx = idx
        if zero_count > 1:
            return [0 for _ in nums]
        if zero_count == 1:
            product_list = [0 for _ in nums]
            product_list[zero_idx] = product_total
            return product_list
        return [product_total // num for num in nums]
# Time complexity:  O(n)
# Space complexity:  O(1)


# Followup ! No division allowed
# You need to use prefix /postfix sum/product strategy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        res = [None] * len(nums)
        for i in range(1, len(nums) - 1):
            res[i] = prefix[i - 1] * suffix[i + 1]
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        return res
# Time complexity:  O(n)
# Space complexity:  O(n)