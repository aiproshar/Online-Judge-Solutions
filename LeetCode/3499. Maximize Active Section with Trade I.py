'''
Initial Complex Solution
Pretty messy
Compression all subsequent 1s and zeros
'''
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        stack = []
        for char in s:
            if char == '0':
                stack.append(0)
            else:
                if stack and stack[-1] != 0:
                    stack[-1] += 1
                else:
                    stack.append(1)
        another = []
        for x in stack:
            if x == 0:
                if another and another[-1] < 0:
                    another[-1] -= 1
                else:
                    another.append(-1)
            else:
                another.append(x)

        ones = 0
        ans = 0
        for num in another:
            if num > 0:
                ones += num
        for i in range(1, len(another) - 1):
            if another[i] > 0:
                ans = max(ans, ones - (another[i - 1] + another[i + 1]))
        return max(ans, ones)
# Time and Space: O(n)


'''
more cleaner implementation
'''
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        i = 0
        zeros = []
        ones = 0
        while i < len(s):
            if s[i] == '0':
                size = 1
                i += 1
                while i < len(s) and s[i] == '0':
                    size += 1
                    i += 1
                zeros.append(size)
            else:
                i += 1
                ones += 1
                continue
        mx = 0
        for i in range(len(zeros) - 1):
            mx = max(mx, zeros[i] + zeros[i+1])
        return mx + ones
