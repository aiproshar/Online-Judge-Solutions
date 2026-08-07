
'''
Classical Brute Force Solution
Three loops, all possible triples, store current closest triplet
Calculate absolute diff on the fly
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest = math.inf
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    diff = abs(target - (nums[i] + nums[j] + nums[k]))
                    if diff < abs(target - closest):
                        closest = nums[i] + nums[j] + nums[k]
        return closest

# Time Complexity: O(n^3)
# Space: O(1)


'''
Optimized solution, two pointer based approach
We ankor K, and for each K static, we iterate i and j 
Becasue its sorted, we can use two pointers to find optimized values for that anchored K
Go through all Ks, we have our optimal
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = math.inf
        for k in range(n):
            i = k + 1
            j = n - 1
            while i < j:
                diff = abs(target - nums[i] - nums[j] - nums[k])
                current = nums[i] + nums[j] + nums[k]
                if diff < abs(target - closest):
                    closest = current
                if current == target:
                    return closest
                elif current > target:
                    j -= 1
                elif current < target:
                    i += 1
        return closest
# Time Complexity: O(n^2)
# Space: O(1)



'''
Can we reduce runtime, not asymptotic bounds
It will still be n^2 but bit faster, any early termintation or other optimization
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = math.inf
        for k in range(n):
            # Quick skipping the duplicates, and doing bakward check so it ensures we processed them at least once
            if k > 0 and nums[k] == nums[k-1]:
                continue
            # in current window minimum possible sum
            # If its already larger than target we bunk
            if k+2 < n and  nums[k] + nums[k+1] + nums[k+2] > target:
                current = nums[k] + nums[k+1] + nums[k+2]
                diff = abs(target - current)
                if diff < abs(closest - target):
                    closest = current
                break
            i = k + 1
            j = n - 1
            while i < j:
                current = nums[i] + nums[j] + nums[k]
                diff = abs(target - current)
                if diff < abs(target - closest):
                    closest = current
                if current == target:
                    return closest
                elif current > target:
                    j -= 1
                elif current < target:
                    i += 1
        return closest

# TC and SC same, but runtime reduced down to 50% for LC test cases average