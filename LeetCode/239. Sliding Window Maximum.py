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

'''
Lazy heap based solution
We push values in heap with index (to invalidate)
Peek root and remove stale entries
'''
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        i = 0
        n = len(nums)
        res = []
        heap = []
        # lazy heap
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        j = k - 1
        i = 0
        while j < n:
            # remove root as long as entry is stale
            while heap:
                max_, max_idx = heap[0]
                if max_idx < i:
                    heapq.heappop(heap)
                else:
                    break
            res.append(-heap[0][0])
            i += 1
            j += 1
            if j >= n:
                break
            heapq.heappush(heap, (-nums[j], j))


        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)


