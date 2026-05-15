# simple if else, use stack (python list can do stack ops in constant time)
# One corner case, trying to pop on empty list
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        open_par = set(['(', '{', '['])
        close_par = set([')', '}', ']'])
        for char in s:
            if char in open_par:
                stack.append(char)
            elif char in close_par:
                # corner case
                if not stack:
                    return False
                if char == ')' and stack[-1] != '(':
                    return False
                elif char == '}' and stack[-1] != '{':
                    return False
                elif char == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True
# Time complexity: O(n)
# Space complexity: O(n)

# cleans Approach
# Huh this is smart
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in pairs:
                # We try to pop, try -> cause we might have an empty list
                if not stack or pairs[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                # We push
                stack.append(char)
        if stack:
            return False
        return True

