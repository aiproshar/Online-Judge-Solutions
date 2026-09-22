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


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        @cache
        def dp(i, j) -> int:

            if j - i + 1 < 3:
                return 0
            if j - i + 1 == 3:
                # two sentinels and one brustable
                return nums[i] * nums[i + 1] * nums[i + 2]
            coins = []
            # skip the sentinels
            for k in range(i + 1, j):
                # inclusive K as sentinel
                # Assume each K will be the last one to pop
                # If K is the last one to pop, only sentinels will remain at left and right
                # So we multiply with the sentinels only
                coin = dp(i, k) + nums[i] * nums[k] * nums[j] + dp(k, j)
                coins.append(coin)
            return max(coins)

        # Adding sentinels
        nums = [1] + nums + [1]
        return dp(0, len(nums) - 1)


# One of the hardest DP, i don't know how i pull this off, took a lot of hints + AI help but code it myself end to end
# Time Complexity: O(n^3), O(n^2) dp states, O(n) work each stare
# Space Complexity: O(n^2), O(n) recursion depth