class Solution:
    def minimumSteps(self, s: str) -> int:

        n = len(s)
        s = list(s)
        steps = 0
        j = 0
        for i in range(n):
            if s[i] == "0":
                continue
            j = max(i + 1, j)
            while j < n:
                if s[j] == "0":
                    s[i], s[j] = s[j], s[i]
                    # non inclusive
                    steps += (j - i)
                    j += 1
                    break
                else:
                    j += 1
        return steps

# Time Complexity: O(n)
# Space Complexity: O(n)



'''
Followup, Constant Space Colution
'''