



"""
Simulation based solution, we just do a simulation, for each batch of n+1, we cannot have a repeat,
So we insert most frequent to least one by one
Put all the inserted to some temp holder until n+1 is done
Apart from the len we also have the whole simulation, if the interviewer asks for simulation this is it
Corner Case: Trim None from the ends
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq = Counter(tasks)
        heap = []
        for task, freq  in task_freq.items():
            heapq.heappush(heap, (freq * -1, task))
        temp = []
        output = []
        while heap:
            i = 0
            while i < n + 1 and heap:
                i += 1
                freq, task = heapq.heappop(heap)
                freq += 1
                output.append(task)
                if freq != 0:
                    temp.append((freq, task))
            while i < n + 1:
                output.append(None)
                i += 1
            while temp:
                heapq.heappush(heap, temp[-1])
                temp.pop()
        while output[-1] is None:
            output.pop()
        return len(output)



# Greedy Approach
# Our freq list length is always <= 26, this makes all sortin, priority queue operations constant (26log26-> constant)
# So, lets just go through the maximum elements first, we pop and reduce the freq
# If freq is 1, we skip. By this we handle the corner case of last iteration, where we dont need IDLE time before cooldown
# If cycle is > 0, that means the number of unique tasks is less than cycle, so we must add IDLE time
# The catch here is calculating time complexity, its linear due to the nature of dataset

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = Counter(tasks)
        heap = [-x[1] for x in freq_dict.items()]
        heapq.heapify(heap)
        idle = 0
        while heap:
            i = n + 1
            temp = []
            while i > 0 and heap:
                i -= 1
                freq = heapq.heappop(heap) * -1
                freq -= 1
                if freq > 0:
                    temp.append(freq * -1)
            # exclude trailing idles, not needed
            if not temp:
                break
            idle += i
            while temp:
                heapq.heappush(heap, temp[-1])
                temp.pop()
        return len(tasks) + idle
