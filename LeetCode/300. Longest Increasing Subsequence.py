'''
Greedy Approach and also Wrong Answer
Input: nums = [0,1,0,3,2,3]
Output: 4  -> 0,1,2,3 (we avoid 3, its non-greedy behavior)
Greedy Approach produces w3, which is wrong
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        global_max = 0
        for i in range(len(nums)):
            last = None
            current_max = 0
            for j in range(i, len(nums)):
                if last is None or nums[j] > last:
                    last = nums[j]
                    current_max += 1
            global_max = max(global_max, current_max)
        return global_max



'''
Backtracking Approach
This is also TLE, searches the whole state space but produces correct result
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def backtrack(start, state) -> int:
            if start == len(nums):
                return len(state) - 1
            # We try to take current element
            lens = []
            if nums[start] > state[-1]:
                state.append(nums[start])
                lens.append(backtrack(start + 1, state))
                state.pop()
            lens.append (backtrack(start + 1, state))
            return max(lens)
        return backtrack(0, [-math.inf])


# Time Complexity: O(2^N)
# Space Complexity: Recursion depth + Path -> O(n)



'''
Classic DP approach
Longest Increasing Subsequence upto i
And we just iterate from begining upto i-1 to find which previous values we can use (satisfies our strict increase)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

# Time Complexity: O(n^2)
# Space Complexity: O(n)