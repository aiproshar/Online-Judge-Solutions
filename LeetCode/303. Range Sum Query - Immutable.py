class NumArray:

    def __init__(self, nums: list[int]):
        # prefix is inclusive
        # add sentinels
        self.prefix = {}
        self.prefix[-1] = 0

        current = 0

        for i in range(len(nums)):
            current += nums[i]
            self.prefix[i] = current

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Time Complexity: O(1) for each sum_range, O(n) for init
# Space: o(n)