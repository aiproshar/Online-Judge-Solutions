
'''
Easy problem, but this is beautiful. Adhoc Array Problem
Just push back the zeor.s to the bottom, and do inplace

Brute Force TLE
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums

# Time Complexity: O(n^2)
# Space: O(1)


'''
Heap based solution
Just push all the zero index in a heap
If we match a nonzero element, find the closes zero and swap it with it
Heap to find the closest in log time
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        heap = []

        for i in range(len(nums)):
            if nums[i] == 0:
                heapq.heappush(heap, i)

        for i in range(len(nums)):
            if nums[i] != 0:
                if heap and heap[0] < i:
                    nums[heap[0]] = nums[i]
                    heapq.heappop(heap)
                    heapq.heappush(heap, i)
                    nums[i] = 0
        return nums
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

'''
The Solution that is most optimnal
Two Pointer based
FIrst pointer, sweeps from start. Secod pointer keeps track of non-zero
When first finds a zero, we swap it with second. Ierate
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        last = -math.inf

        for i in range(len(nums)):
            if nums[i] == 0:
                if last <= i:
                    last = i + 1
                for j in range(last, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        last = j + 1
                        break
                else:
                    break
        return nums


# Time Complexity: O(n)
# Space: O(1)