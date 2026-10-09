'''
Brute Force Approach
Take a slice of each slide, sort, calculate median

'''


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:

        res = []
        for i in range(len(nums) - k + 1):

            current = nums[i:i + k]
            current.sort()
            if k % 2 == 0:
                res.append((current[k // 2] + current[k // 2 - 1]) / 2)
            else:
                res.append(current[k // 2])
        return res

# Time Complexity: O(n * klogk)
# Space: O(k)
# TLE