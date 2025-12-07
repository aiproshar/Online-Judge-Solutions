
#QoL improvement, first python solution
#After messing up meta interview, specially due to C++, i am switching to python for DSA rounds
#Python aint that bad after all, will write a ML Service API server soon


# Greedy Approach
# Our freq list length is always <= 26, this makes all sortin, priority queue operations constant (26log26-> constant)
# So, lets just go through the maximum elements first, we pop and reduce the freq
# If freq is 1, we skip. By this we handle the corner case of last iteration, where we dont need IDLE time before cooldown
# If cycle is > 0, that means the number of unique tasks is less than cycle, so we must add IDLE time
# The catch here is calculating time complexity, its linear due to the nature of dataset
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        freq = [-x[1] for x in freq.items()]

        heapq.heapify(freq)
        time = 0
        while freq:
            cycle = n + 1
            store = []
            while cycle > 0 and freq:
                top = heapq.heappop(freq) * -1
                if top > 1:
                    store.append(top - 1)
                cycle -= 1
            if store == []:
                break
            if cycle != 0:
                time += cycle
            for item in store:
                heapq.heappush(freq, item * -1)
        return time + len(tasks)
