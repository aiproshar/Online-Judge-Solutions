class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:

        heap = []

        for i in range(len(nums)):

            num = nums[i]
            num_str = sorted(str(num), reverse=True)
            num_arranged = int("".join(num_str))
            delta = num_arranged - num
            # min heap, traping the max values
            heapq.heappush(heap, (delta))
            if len(heap) > k:
                heapq.heappop(heap)
        total = sum(nums)

        while heap and k >  0:
            delta = heapq.heappop(heap)
            total += delta
            k -= 1

        return total

# heap based solution, beautiful. Sort will also work
# Time Complexity: nlogk
# Space Complexity: O(n)
