'''
Ez Ad hoc Problem
Instead of Two Loops/ Sorting, we just do a two pass
Find 2 largest number and we have answer
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        index = set()
        mx = 0
        for i in range(len(nums)):
            if nums[i] > nums[mx]:
                mx = i
        first = mx
        mx = None
        for i in range(len(nums)):
            if mx is None:
                if i != first:
                    mx = i
                    continue
                else:
                    continue
            elif nums[i] > nums[mx] and i != first:
                mx = i
        return (nums[mx] - 1) * (nums[first] - 1)
# Time Complexity: O(n)
# Space Complexity: O(1)


'''
As my code is a clutter mess, there is a better way to write the same logic flow

Code by Gemini Pro 
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0

        for num in nums:
            if num > max1:
                # Push the old max down to second place
                max2 = max1
                max1 = num
            elif num > max2:
                # Update second place
                max2 = num

        return (max1 - 1) * (max2 - 1)