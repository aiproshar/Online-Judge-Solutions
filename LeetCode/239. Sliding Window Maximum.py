# dumbfuck solution
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        que = deque()
        ans = []
        for i in range(k):
            que.append(nums[i])
        ans.append(max(que))
        for i in range(k, len(nums)):
            que.popleft()
            que.append(nums[i])
            ans.append(max(que))
        return ans


# Time complexity: O(n*K)
# Space complexity: O(1) or O(n) because of result array




# Faster solution, linear
# We use monotonic deque, a variant of monotonic stack. Stack but we can chop from bottom if you know
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        sliding_max = []

        for i in range(k):
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])

        sliding_max.append(que[0])
        for i in range(k, len(nums)):
            # cleanup previous state
            if que[0] == nums[i - k]:
                que.popleft()
            # exec current state
            while que and nums[i] > que[-1]:
                que.pop()
            que.append(nums[i])
            sliding_max.append(que[0])
        return sliding_max

# Time complexity: O(n)
# Space complexity: O(k) # at most k items in stack, we get rid of it




