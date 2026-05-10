# naive bruteforce approach
# All possible combination, add them to a set to avoid duplicates
# Pythonista Way
# TLE

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        ans.add(tuple(triplet))

        ans_list = [list(x) for x in ans]
        return ans_list
# Time complexity: O(n^3)
# Space complexity: O(n)


# converting three sumt o two dum
# pin one element, and it becomes two sum problem
# sort it so we can use two pointer two sum style
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        nums.sort()
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:  # TLE without this optimization
                continue
            target = -nums[x]
            i = x + 1 #initially i always started i from 0, which was a mistake
                        # We already explored previous elements of current x by pinning it
            j = len(nums) - 1

            while i < j:
                if nums[i] + nums[j] == target:
                    if i != x and j != x:
                        triplet = [nums[i], nums[j], nums[x]]
                        triplet.sort()
                        ans.add(tuple(triplet))
                        i += 1
                        j -= 1
                    elif i == x:
                        i += 1
                    elif j == x:
                        j -= 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1

        ans = [list(item) for item in ans]
        return ans

# Time complexity: O(n^2)
# Space complexity: O(n)



# most optimized solution
# We don't need that set unique drama at all
# Avoid duplicate everywhere
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:  # TLE without this optimization
                continue
            target = -nums[x]
            i = x + 1
            j = len(nums) - 1

            while i < j:
                if nums[i] + nums[j] == target:
                    triplet = [nums[i], nums[j], nums[x]]
                    ans.append(triplet)
                    while i+1 < len(nums) and nums[i+1] == nums[i]: #pass duplicates
                        i+=1
                    while j-1 >= 0 and nums[j-1] == nums[j]: #pass duplicates
                        j-=1
                    i+=1 # corner case: you came to the last duplicate, now discard it
                    j-=1 #Or We can stick in a infinite loop
                elif nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
        return ans
# Time complexity: O(n^2), but highly optimized
# Space: O(1), but if we consider modification of the input, then O(n)