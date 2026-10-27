class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot = None
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if pivot is not None:
                break
            if nums[i] < nums[i + 1]:
                pivot = i
                # find the smallest number which is larger than pivot
                for j in range(n - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

        if pivot is None:
            nums.reverse()
            return

        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)