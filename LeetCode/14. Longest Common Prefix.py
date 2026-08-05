
'''
EZ bruteforce Array Problem
Slight Optimization Scope
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(x) for x in strs])
        lcp = []
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return "".join(lcp)
            lcp.append(strs[0][i])
        return "".join(lcp)

# Time Complexity: O(S) where S is all characters combined, eg:["arafat" , "arafat" , "arafat" , "arafat"]
# Space: O(m) where m is len of common prefix