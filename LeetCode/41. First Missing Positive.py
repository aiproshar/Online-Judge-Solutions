
'''
Geenral Solution
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        visited = set()
        mx = 0
        for num in nums:
            if num > 0:
                visited.add(num)
                mx = max(mx, num)
        for i in range(1, mx + 1):
            if i not in visited:
                return i
        return mx + 1


# Time and Space Complexity: O(1)


'''
Optimal Solution using Constant Space
Fqv to building a hashtable, where key is index (0 based), value is that number if that exists
'''


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(len(nums)):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Corner Case: You must look at the value we just swap, that may sit in some places too
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
                '''
                using for loop and then i-=1 inside does not work, for loop immmune
                overwritten i does on that iteration
                '''

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return nums[-1] + 1

# Time Complexity: O(1)
# Space Complexity: O(1)