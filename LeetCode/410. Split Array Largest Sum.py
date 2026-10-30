'''
A True Leetcode Hard, minimization + maximization hybrid problem, DP


The intuition is we need to split k items, means we need k-1 index, o:k and k:-1, one index two split

So what's the DP state, we need to split the current slice into k items

We can pick any index of current slice to split, recursively call. Reduce how many slices we need to make

Base cases: k is zero so no more slicing is required, return sum
k > 0 but slice len is < 2, we cannot split it up. Return inf, tha'ts a invalid number

If we decide to slive at K, we must take the max of current split recursively calling the other slpit
'''


# Highly inefficient, but the intuition and backbone is almost perfect
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        @cache
        def dfs(nums, k) -> int:
            if k == 0:
                return sum(nums)
            if len(nums) < 2 and k != 0:
                return math.inf
            res = []
            for i in range(1,len(nums)):
                res.append(
                    # All magic is here
                    max(sum(nums[:i]), dfs(tuple(nums[i:]), k-1))
                )
            return min(res)
        return dfs(tuple(nums), k-1)

# n*k total states, but we do a lot of slice operation each state, and do this for n times. ALso sum operation
# For n times, where each sum is O(n) on its own
# So on each state, we do n^2
# So Time Complexity: state * work each state, (nk)(n^2) -> n^3*k
# Space Complexity: O(n*k) state space, plus K depth at max, but each state can be n, so n^2*k + k recursion depth




'''
Improving state space complexity
Instead of slice as tuple, i just need the start index here
So that's what we do
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(len(nums)):
            # sum(nums[a:b]) == prefix[b] - prefix[a]
            pre[i+1] = pre[i] + nums[i]

        @cache
        def dfs(start, k) -> int:
            if k == 0:
                #return sum(nums[start:])
                return pre[n] - pre[start]
            if len(nums) - start < 2 and k != 0:
                return math.inf
            res = []
            for i in range(start+1,n):
                res.append(
                    max(
                        #sum(nums[start:i]),
                        pre[i] - pre[start],
                        dfs(i, k-1)
                        )
                )
            return min(res)
        return dfs(0, k-1)

# Expensive slicing operation is gone, but still we are doing sum operation n times on each state
# So TC remains same, O(n^3 * k)
# Space: Our state Space key is now constant, not linear. So O(n*k) + k recursion depth


'''
Prefix sum to reduce hungry sum computation
Everything else same
'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(len(nums)):
            # sum(nums[a:b]) == prefix[b] - prefix[a]
            pre[i+1] = pre[i] + nums[i]

        @cache
        def dfs(start, k) -> int:
            if k == 0:
                #return sum(nums[start:])
                return pre[n] - pre[start]
            if len(nums) - start < 2 and k != 0:
                return math.inf
            res = []
            for i in range(start+1,n):
                res.append(
                    max(
                        #sum(nums[start:i]),
                        pre[i] - pre[start],
                        dfs(i, k-1)
                        )
                )
            return min(res)
        return dfs(0, k-1)
# Time Complexity: n*k states, running a loop of n each state. So O(n^2 * k)
# Space: same as previous. O(nk) + K recursion depth
# We can remove res array, amybe keep just the minimum. That also works



'''
Binary Search Based Solution
Weird
Same as Capacity to ship K packages in D days, line by line same
'''


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def isValid(max_sum: int) -> bool:

            current = 0
            array_count = 1
            for num in nums:
                current += num
                if current > max_sum:
                    current = num
                    array_count += 1
            return array_count <= k

        lo = max(nums)
        hi = sum(nums) + 1

        while lo < hi:
            mid = (lo + hi) // 2
            if isValid(mid) is False:
                lo = mid + 1
            else:
                hi = mid
        return lo

# Time Complexity: O(nlog(sum(nums))
# Space Complexity: O(1)