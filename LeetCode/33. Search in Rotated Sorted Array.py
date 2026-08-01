class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo < hi - 1:
            mid = (lo + hi) // 2
            if nums[lo] > nums[mid]:
                hi = mid
            else:
                lo = mid
        split_idx = None
        if nums[lo] > nums[hi]:
            split_idx = lo
        else:
            split_idx = hi

        def bi_search(nums, target):
            lo = 0
            hi = len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        x = bi_search(nums[:split_idx + 1], target)
        y = bi_search(nums[split_idx + 1:], target)

        if y != -1:
            return y + split_idx + 1
        return x




