# Generic Solution
# Sort the whole thing
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        freq = [(key, val) for key,val in freq.items()]
        freq = sorted(freq, key=lambda x: (-x[1], x[0]))
        freq = [x[0] for x in freq]
        return freq[:k]
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Heap Based Approach
# Helps a bit of time and space complexity when n >>> k (top 5 out of million elements), but difficult

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        return heapq.nsmallest(k, freq.keys(), key=lambda x: (-freq[x], x))
# This is the best solution, to be honest
# Time: O(n) + (nlogk) or O(n + ulogk) where u is unique elements, there also string compare factor,
# We also need to take that