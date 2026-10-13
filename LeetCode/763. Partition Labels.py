'''
Freq counter based solution
'''

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        inside = set()
        res = []
        current_len = 0
        last_idx = {}
        # keeping track of last idx
        for i in range(len(s)):
            last_idx[s[i]] = i

        for i in range(len(s)):
            current_len += 1
            inside.add(s[i])
            # if we reached a last index,
            # remove if from the inside
            if last_idx[s[i]] == i:
                inside.discard(s[i])
                if not inside:
                    res.append(current_len)
                    current_len = 0
        return res

# Time Complexity: O(n)
# Space Complexity: O(1) cause keyspace is bounded by 26, res is also bounded by 26

'''
Keep track of last index
If we find 'a' and it's the last occurrence remove it from inside
'''
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        inside = set()
        res = []
        current_len = 0
        last_idx = {}
        # keeping track of last idx
        for i in range(len(s)):
            last_idx[s[i]] = i

        for i in range(len(s)):
            current_len += 1
            inside.add(s[i])
            # if we reached a last index,
            # remove if from the inside
            if last_idx[s[i]] == i:
                inside.discard(s[i])
                if not inside:
                    res.append(current_len)
                    current_len = 0
        return res

# Time Complexity: O(n)
# Space Complexity: O(1)