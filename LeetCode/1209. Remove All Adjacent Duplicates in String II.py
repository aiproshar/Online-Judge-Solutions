'''
Straight forward stack solution
'''
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack:
                stack.append([char, 1])
            else:
                if stack[-1][0] == char:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([char, 1])

        str_list = []

        for char, freq in stack:
            for _ in range(freq):
                str_list.append(char)

        return "".join(str_list)

# Time Complexity: O(n)
# Space Complexity: O(n)