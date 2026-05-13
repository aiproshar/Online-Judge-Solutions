# Brute force all possible substr generate and compare
# Really dumb but correct
# TLE
class Solution:
    def isSubstr(self, freq: defaultdict, freq_t: defaultdict) -> bool:
        for key, val in freq_t.items():
            if val > freq[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        freq_t = defaultdict(lambda: 0)

        for char in t:
            freq_t[char] += 1

        min_idx = None
        min_len = float('inf')
        for i in range(len(s)):
            freq = defaultdict(lambda: 0)
            for j in range(i, len(s)):
                freq[s[j]] += 1
                if self.isSubstr(freq, freq_t):
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        min_idx = (i, j)
        if min_idx is not None:
            return s[min_idx[0]:min_idx[1] + 1]
        return ""
# Time complexity: O(n^2)
# Space complexity: O(1) -> dicts are constant key space