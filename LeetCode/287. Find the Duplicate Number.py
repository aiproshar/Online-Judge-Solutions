
# Not a great fan of this problem
# Can be easily done by bruteforce in constant space, or linear time in linear space
# Linear: just use a set

# Brute Force TLE
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1, n + 1):
            count = 0
            for j in range(i, n):
                if nums[j] == i:
                    count += 1
                    if count > 1:
                        return i
# Time: O(n^2)
# Space: O(1)

# using a set: Time: O(n) space: O(n)

# Remember

# Constant Space and linear time
# When you hear constant space and linear time, its usually floyd (slow-fast pointer)
# Or two pointers or sum or some other stuffs!
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        slow = nums[slow]
        fast = nums[0]
        fast = nums[nums[fast]]

        while fast != slow:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
# Time: O(n) Space: O(1)



'''
Using Floyd's cycle detection Algorithm
There is a cycle that is guranteed, we need to find where is the cycle

0 → 1 → 3 → 2 → 4
                │
                │ nums[4] = 2
                ▼
                2   ← back to the "2" node (loop entrance)


            
              loop
           ┌────────┐
0 → 1 → 3 → 2 → 4 ──┘
            ▲
         entrance = duplicate = 2
         
         
0 → 1 → 3 → 2 → 4 ──┐
            ▲       │
            └───────┘
       Floyd returns 2 (entrance),
       not 4 (the one that loops back)
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


