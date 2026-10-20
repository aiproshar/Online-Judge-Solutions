'''
Initial simulation based solution

Was a bit inefficient cause we sort all the numbers every time, and it caused TLE
'''


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:

        min_range = [-math.inf, math.inf]
        current = [0] * len(nums)

        while True:

            temp = []

            for i in range(len(nums)):
                temp.append((nums[i][current[i]], i))

            temp.sort(key=lambda x: x[0])
            min_value, min_idx = temp[0]
            max_value, max_idx = temp[-1]

            if max_value - min_value < min_range[1] - min_range[0]:
                min_range = [min_value, max_value]

            # increase the min value in hope we can reduce the range
            current[min_idx] += 1
            if current[min_idx] == len(nums[min_idx]):
                break

        return min_range
# n = len of lists (max). Total items n*k where k is no of list
# Time Complexity: O(klogk * nk)
# Space Complexity: O(k)

'''
Heap Optimized solution
min_heap + track max as new values are larger
'''
class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:

        min_range = [-math.inf, math.inf]
        current = [0] * len(nums)

        min_heap = []
        current_max = -math.inf
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i))
            current_max = max(current_max, nums[i][0])

        while True:

            min_value, min_idx = heapq.heappop(min_heap)
            if current_max - min_value < min_range[1] - min_range[0]:
                min_range = [min_value, current_max]

                # increase the min value in hope we can reduce the range
            current[min_idx] += 1
            if current[min_idx] == len(nums[min_idx]):
                break
            else:
                current_max = max(current_max, nums[min_idx][current[min_idx]])
                heapq.heappush(min_heap, (nums[min_idx][current[min_idx]], min_idx))

        return min_range

# Time Complexity: O(n*k * logk)
# Space: O(k)