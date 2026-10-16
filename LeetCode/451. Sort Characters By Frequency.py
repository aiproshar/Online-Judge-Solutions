'''

'''


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq = [(char, count) for char, count in freq.items()]
        freq.sort(key=lambda x: (-x[1], x[0]))

        res = []
        for char, count in freq:
            for i in range(count):
                res.append(char)

        return "".join(res)
# Time Complexity: O(nlogn)
# Space: O(n)