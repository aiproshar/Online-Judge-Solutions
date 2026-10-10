'''
Lazy heap deletion based solution
Not optimal, memory bloat
This is a TRUE hard problem !
'''
class LFUCache:

    def __init__(self, capacity: int):

        # (freq, key) -> we find the lowest freq at top, key to identify whom to evict
        self.heap = []
        self.cap = capacity
        # key -> freq, value. freq discard stale heap entries, freq only increases
        self.freq = {}
        self.timestamp = 0


    def get(self, key: int) -> int:

        if key in self.freq:
            freq, value = self.freq[key]
            self.timestamp += 1
            heapq.heappush(self.heap, (freq + 1, self.timestamp, key))
            self.freq[key] = [freq + 1, value]
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.freq:
            # just update
            freq, _ = self.freq[key]
            self.timestamp += 1
            heapq.heappush(self.heap, (freq + 1, self.timestamp ,key))
            self.freq[key] = [freq + 1, value]
            return None
        else:
            # we create a new entry
            # check for eviction fist and then we insert
            # if we insert before eviction our newest insert gets kicked
            if len(self.freq) == self.cap:
                # at cap, make a room for one
                while self.heap:
                    freq_, _, key_ = heapq.heappop(self.heap)
                    # check if stale entry
                    if key_ not in self.freq or freq_ != self.freq[key_][0]:
                        continue
                    else:
                        # delete the key, evict
                        del self.freq[key_]
                        break
            self.timestamp += 1
            heapq.heappush(self.heap, (1, self.timestamp, key))
            self.freq[key] = [1, value]
            return None


# Time Complexity: logn, where n is the number of get/put operations called upto now
# Put can trigger nlogn due to cleanup but its amortized over n operations. So its logn is justified
# Space: O(n) where n is the number of get/put operations called upto now