class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = []
                while stack[-1] != "[":
                    substr.append(stack.pop())
                stack.pop()
                # find freq
                freq = []
                while stack and "0" <= stack[-1] <= "9":
                    freq.append(stack.pop())
                if freq == []:
                    freq = 1
                else:
                    freq = int("".join(freq[::-1]))
                substr = substr[::-1] * freq

                for char in substr:
                    stack.append(char)
        return "".join(stack)

# Time Complexity: O(n + N * d) where n is original chars, d is max bracket nesting and N is output size
# Space Complexity: O(N)