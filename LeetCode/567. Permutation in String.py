# combination of both substring and anagram
# A bit complex, needs to define compare of two dict


class Solution:
    def isZero(self, s1: defaultdict, s2: defaultdict) -> bool:
        for key, val in s1.items():
            if s2[key] != val:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        freq_s1 = defaultdict(lambda: 0)
        freq_s2 = defaultdict(lambda: 0)

        for char in s1:
            freq_s1[char] += 1

        for char in s2[:len(s1)]:
            freq_s2[char] += 1

        if self.isZero(freq_s1, freq_s2):
            return True
        left = 0
        right = len(s1) - 1

        while right + 1 < len(s2):
            freq_s2[s2[left]] -= 1
            freq_s2[s2[right + 1]] += 1
            if self.isZero(freq_s1, freq_s2):
                return True
            left += 1
            right += 1
        return False
# Time complexity: O(n) -> two pointer one pass
# Space complexity: O(1) -> Yes, because keys are constant space, only 26 letter