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
        n = len(nums)
        left_list = [None] * n
        right_list = [None] * n
        left_list[0] = nums[0]  # 1,0,0,0
        right_list[n - 1] = nums[n - 1]  # 0,0,0,4

        i = 1
        while i < len(nums):
            left_list[i] = nums[i] * left_list[i - 1]
            i += 1

        i = n - 2
        while i >= 0:
            right_list[i] = nums[i] * right_list[i + 1]
            i -= 1

        product_array = []

        for idx, _ in enumerate(nums):
            left = left_list[idx - 1] if idx - 1 >= 0 else 1
            right = right_list[idx + 1] if idx + 1 < len(right_list) else 1
            product_array.append(left * right)
        return product_array
# Time complexity:  O(n)
# Space complexity:  O(n)