'''
Bruteforce Backtrack Solution
Explore all possible state space tree
TLE, a big one
'''


class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        def backtrack(nums) -> int:
            if len(nums) <= 2:
                return 0
            res = []
            for i in range(1, len(nums) - 1):

                current = nums[i - 1] * nums[i] * nums[i + 1]
                temp = []
                for k in range(len(nums)):
                    if k == i:
                        continue
                    else:
                        temp.append(nums[k])

                res.append(current + backtrack(temp))
            return max(res)

        nums = [1] + nums + [1]
        return backtrack(nums)
# Time Complexity: n choices * n-1 choices * .....3*2*1 and n work each step. Goes to O(n!)
# Space Complexity: Recursion depth: O(n), each comes with an array of n len as parameter, so  O(n^2)