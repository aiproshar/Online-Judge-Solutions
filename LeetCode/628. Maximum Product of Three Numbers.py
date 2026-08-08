'''
Easy, you just need the right intuition
Max Product can be based on largest 3 integers, or smallest 2 integers which are negative, cancels the minus
and mul with the largest positive
'''
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[0] * nums[1] * nums[-1],
            nums[-1] * nums[-2] * nums[-3]
        )
# Time Complexity: nlogn
# Space Complexity: O(n) for timsort, O(1) in general
'''
There is some linear time solution, which is not good. Messy code, passing the array 3 times this trick
Avoiding that solution
'''