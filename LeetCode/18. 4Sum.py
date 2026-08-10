
'''
Brute Force Approach
Sort so we avoid duplicates
Also we don't skip so back that its actually previous anchor

1,2,3,3,4
    i j
We don't want j to move forward comparing with i

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if j-1 > i and nums[j-1] == nums[j]:
                    continue
                for k in range(j+1, n):
                    if k-1 > j and nums[k-1] == nums[k]:
                        continue
                    for l in range(k+1, n):
                        if l-1 > k and nums[l-1] == nums[l]:
                            continue
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            res.append([
                                nums[i],
                                nums[j],
                                nums[k],
                                nums[l]
                                ])
        return res
# Time Complexity: O(n^4)
# Space Complexity: O(n)

'''
3 sum inspired solution, reducing one polynomial
FOr every i and j, two pointer for k and l
Corner case: Avoid duplicates, also dont skip when duplicates are not your range
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, n):
                if j - 1 > i and nums[j - 1] == nums[j]:
                    continue

                partial = target - (nums[i] + nums[j])
                # So this is now a two sum problem
                k = j + 1
                l = n - 1
                while k < l:
                    if k - 1 > j and nums[k - 1] == nums[k]:
                        k += 1
                        continue
                    if l < n - 1 and nums[l] == nums[l + 1]:
                        l -= 1
                        continue

                    if nums[k] + nums[l] == partial:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                    elif nums[k] + nums[l] > partial:
                        l -= 1
                    else:
                        k += 1
        return res
# Time Complexity: O(n^3)
# Space Complexity: O(n)
# Some further early termination optimization is possible