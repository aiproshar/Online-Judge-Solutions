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
        # timestamp as tiebreaker, as min heap, old accessed entries first during freq tie
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



'''
Actually not that hard using ordered dict
The main thing is handling the min_freq logic
Also we empty the buckets when there is no item

'''


class LFUCache:

    def __init__(self, capacity: int):
        # freq -> key:value ordered dict, maintains insertion order
        self.data = defaultdict(collections.OrderedDict)
        # key -> freq mapping, to find freq bucket
        self.freq = {}
        # From where we evict
        self.min_freq = 1
        # to trigger evict event
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.freq:
            freq = self.freq[key]
            value = self.data[freq][key]

            # remove from current freq bucket
            del self.data[freq][key]
            # no element in freq bucket, remove it
            if len(self.data[freq]) == 0:
                del self.data[freq]
                # update min_freq if current_freq is minimum by +1
                if self.min_freq == freq:
                    self.min_freq += 1

            # add to the next freq bucket
            self.data[freq + 1][key] = value
            self.freq[key] = freq + 1
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.freq:
            # we need to update, move the key to next bucket, remove from current
            freq = self.freq[key]
            del self.data[freq][key]
            self.data[freq + 1][key] = value
            self.freq[key] = freq + 1
            # bucket cleanup if needed
            if len(self.data[freq]) == 0:
                del self.data[freq]
                # check if freq was minimum
                if freq == self.min_freq:
                    self.min_freq += 1
        else:
            # we need to insert a new item
            # check if we already at capacity, make a space
            # min_freq is now 1
            if len(self.freq) == self.cap:
                # the key we evict
                key_evict, _ = self.data[self.min_freq].popitem(last=False)
                del self.freq[key_evict]
                # bucket cleanup if needed after removal item from min_freq bucket
                if len(self.data[self.min_freq]) == 0:
                    del self.data[self.min_freq]

            # lets insert fresh item
            self.data[1][key] = value
            self.freq[key] = 1
            self.min_freq = 1
        return None

#  Time Complexity: Get/Put: O(1)
# Space Complexity: O(n), n = total no of keys

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)