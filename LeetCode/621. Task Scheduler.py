"""
Simulation based solution, we just do a simulation, for each batch of n+1, we cannot have a repeat,
Greedy Heap based approach
If we need to fill n+1 len task packet of unique tasks, we take from most frequent to least
That's IT
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        heap = [-val for key, val in freq.items()]
        heapq.heapify(heap)
        total = 0
        while heap:
            # n gapes, inclusive then its n+1
            cycle = n + 1
            visited = []
            while cycle > 0 and heap:
                # Pop most freqient element and decrease cycle
                # Temporarily store t visited
                visited.append(heapq.heappop(heap))
                cycle -= 1
                total += 1
            for item in visited:
                # Must make sure it is not reduced to zero
                if item + 1 < 0:
                    heapq.heappush(heap, item+1)
            # The most important line, if we have elements left in heap means we need another cycle
            # Were we able to fill current cycle with unique elements, if not then we add null
            # This is literally the nulls we are adding
            if heap:
                total += cycle
        return total

# Time Complexity: O(nlog26)
# Space: O(26)


from typing import List
from collections import Counter

'''
Math-Based Solution Strategy:
We build the schedule framework around the most frequent task(s).
Example: If 'A' appears 4 times and n=2, the layout looks like this:
A _ _ | A _ _ | A _ _ | A
(Chunk 1) (Chunk 2) (Chunk 3) (Last Cycle)

If 'A' and 'B' both appear 4 times (tie for most frequent):
A B _ | A B _ | A B _ | A B
'''


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Step 1: Count how many times each task appears
        freq = Counter(tasks)

        # Step 2: Extract just the counts (we don't care about the letter names)
        # and sort them in descending order so the biggest number is at freq[0]
        freq = [x for x in freq.values()]
        freq.sort(reverse=True)

        # Step 3: Figure out how many tasks tie for the "most frequent" spot
        max_no = 0
        for item in freq:
            if item == freq[0]:
                max_no += 1
            else:
                # Since the list is sorted, once we see a smaller number, we can stop
                break

        # Step 4: Calculate the required time based on our chunks
        #
        # (freq[0] - 1) -> The number of full chunks/intervals.
        #                  If a task appears 4 times, there are 3 chunks between them.
        #
        # (n + 1)       -> The size of each chunk.
        #                  1 slot for the task itself + 'n' slots for the cooldown period.
        #
        # max_no        -> The size of the final cycle.
        #                  The last group doesn't need trailing idle time. If only 'A'
        #                  is the most frequent, we just add 1. If 'A' and 'B' tie, we add 2.
        min_time = (freq[0] - 1) * (n + 1) + max_no

        # Step 5: Handle edge cases where there are zero idle slots
        #
        # If min_time is smaller than the total number of tasks, it means we have so
        # many diverse tasks that they fill up all the idle slots and then some.
        # In this case, we don't need any idle time at all, so the answer is just the
        # total number of tasks.
        return max(min_time, len(tasks))

# Time Complexity: O(n) where n == len(tasks
# Space: O(26)