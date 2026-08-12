'''
One of the most beautiful problems, sliding window


Inital Brute force, eval all subarray, TLE
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product = product * nums[j]
                if product < k:
                    res += 1
                else:
                    break
        return res
# Time Complexity: O(n)
# Space Complexity: O(1)


'''
I dont know, maybe i am doing to much dp problems these days, coming up with DP solution for every problem
But this was a bad solution
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        count = 0
        total_prod = math.prod(nums)

        def dfs(start, end, current):
            nonlocal count
            if current > k:
                count += 1
            else:
                return
            if start > end:
                return
            temp = current // nums[start]
            dfs(start + 1, end, temp)
            temp = current // nums[end]
            dfs(start, end - 1, temp)

        dfs(0, n - 1, total_prod)
        return ((n * (n + 1)) // 2) - count

# Time and Space: Pretty BAD ! Jost avoid. This is for referee over complex solution example




'''
Optimal Solution
Idea: Our new element extends existing n items with n subarray, 
1,2,3,4 -> We add 5 so 5, 54, 543, 5432, 54321. So we have new n subarrays YaY
if j < i -> invalid state, current window is empty. This is corner case
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k in {0, 1}:
            return 0

        n = len(nums)
        product = 1

        i = j = 0
        total = 0
        while j < n:
            product *= nums[j]
            # invalid state
            while product >= k and i < n:
                product = product // nums[i]
                i += 1
            total += j - i + 1
            j += 1
# Time Complexity: O(n)
# Space Complexity: O(1)