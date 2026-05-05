
# We need a UUID for a anagram group, if we lexicographically sort any anagram, its same stuff
# So we insert each string to a dict, where key is signature, UUID, sorted string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angs = defaultdict(list)
        for word in strs:
            signature = "".join(sorted(word))
            angs[signature].append(word)
        ans = []
        for _, val in angs.items():
            ans.append(val)
        return ans
# Time: O(NK log K) - N = number of strings, K = max string length (worst case)
# Space: O(NK) [N words, worst case all are K length]

