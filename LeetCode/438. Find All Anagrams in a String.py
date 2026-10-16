class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:

        if len(s) < len(p):
            return []
        freq_s = Counter(s[:len(p)])
        freq_p = Counter(p)
        res = []
        if freq_s == freq_p:
            res.append(0)
        i = 1
        while i + len(p) - 1 < len(s):
            freq_s[s[i - 1]] -= 1
            freq_s[s[i + len(p) - 1]] += 1
            if freq_s == freq_p:
                res.append(i)
            i += 1
        return res


# Time Complexity: O(n)
# Space Complexity: O(1)