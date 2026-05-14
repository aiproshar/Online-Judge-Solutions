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



# Followup of reduced time complexity -> linear time
# Grow and shrink phase, grow until we have a match, then shrink as long as match is true
# Handled edge cases of growing to the end and not finding any match after reaching and
# Handled edge case of invalid inpur (substr is larger), early termination
class Solution:
    def isSubstr(self, freq: defaultdict, freq_t: defaultdict) -> bool:
        for key, val in freq_t.items():
            if val > freq[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        freq_t = defaultdict(lambda: 0)
        freq = defaultdict(lambda: 0)

        for char in t:
            freq_t[char] += 1

        i = j = 0
        freq[s[0]] = 1
        min_idx = None
        min_len = float('inf')
        while j < len(s):
            # grow phase
            # Bound check needed
            while not self.isSubstr(freq, freq_t) and j + 1 < len(s):
                j += 1
                freq[s[j]] += 1

            # We grew to the end but what if no match ?
            if not self.isSubstr(freq, freq_t):
                break

            # shrink phase
            while self.isSubstr(freq, freq_t):
                freq[s[i]] -= 1
                i += 1
            i -= 1
            freq[s[i]] += 1
            if j - i + 1 < min_len:
                min_len = j - i + 1
                min_idx = (i, j)
            # shift phase, shift right by one, inhope of a new substr
            # Bound check needed
            if j + 1 == len(s):
                break
            freq[s[i]] -= 1
            i += 1
            j += 1
            freq[s[j]] += 1
        if min_idx is not None:
            return s[min_idx[0]:min_idx[1] + 1]
        return ""
# Time Complexity: O(n * 26) # We have a constant overhead, we do repetitive compare every time
# Space complexity: O(26) -> Keyspace is constant

# More improvement -> use match counter, keep the freq dicts but only update the modified chars in O(1) , so we know how many match in constant time