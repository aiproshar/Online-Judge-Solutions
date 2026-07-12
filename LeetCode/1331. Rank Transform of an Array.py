'''
EZ basic list and sorting stuff
'''
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(list(set(arr)))
        ranks = {}
        for i in range(len(arr_sorted)):
            ranks[arr_sorted[i]] = i + 1
        res = []
        for num in arr:
            res.append(ranks[num])
        return res

# Time Complexity: O(nlogn)
# Space Complexity: O(n)
