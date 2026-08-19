'''
Initial Solution, a bit bruteforce and no pruning
We generate all possible subset and when we reach end, we sort the current and
put it in a set so that we avoid having duplicates
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(i, current):
            if i == len(nums):
                temp = current.copy()
                temp.sort()
                res.add(tuple(temp))
                return
            # take current one
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
            # skip current one
            backtrack(i + 1, current)

        backtrack(0, [])
        return [list(x) for x in res]

# Time Complexity: O(2^N * nlogn
# Space Complexity: O(2^N * N)

'''
So how we avoid the duplicates, same strategy as Combinatorics Sum II : https://github.com/aiproshar/Online-Judge-Solutions/blob/master/LeetCode/40.%20Combination%20Sum%20II.py
The strategy is simple, if we skip we skip all similar numbers continuously, that's the main logic
More in depth explain on Combinatorics Sum II
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(i, current):
            if i == len(nums):
                res.append(current.copy())
                return
            # take the current element
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

            # skip the current and all its dupes
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, current)

        backtrack(0, [])
        return res

# Time Complexity: O(2^N * N)
# Space: O(2^N * N) for result array, aux space is O(N) recursion depth