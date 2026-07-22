
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


'''
Some More optimized way, skips sorting
We need to generate a signature without any kind of sort
What if we serialize a list of freq counters, so all anagrams have same signature
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for word in strs:
            signature = [0] * 26
            for char in word:
                signature[ord(char) - ord('a')] += 1

            signature = "#".join([str(x) for x in signature])
            anagrams[signature].append(word)
        res = []
        for value in anagrams.values():
            res.append(value)
        return res

# Time Complexity: O(nk)
# Space Complexity: O(nk)