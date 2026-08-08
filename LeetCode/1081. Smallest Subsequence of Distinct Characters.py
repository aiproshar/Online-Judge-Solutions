
'''
First intuition, backtrack based approach
If current character is not already in the state, we have 2 choices,
- Take it
- Don't take it, hoping that we might see this in future
Kind of bruteforce, generates all possible scenarios
'''
class Solution:
    def smallestSubsequence(self, s: str) -> str:

        smallest = None
        unique = len(set(list(s)))
        def backtrack(i, current):
            nonlocal smallest
            if len(current) == unique:
                sub_seq = "".join(current)
                if smallest is None or sub_seq < smallest:
                    smallest = sub_seq
                return
            if i >= len(s):
                return
            if s[i] in current:
                backtrack(i+1, current)
            else:
                current.append(s[i])
                backtrack(i+1, current)
                current.pop()
                backtrack(i+1, current)
        backtrack(0, [])
        return smallest


# Time Complexity: O(2^n)
# Space: O(n)





'''
Greedy Approach, which is efficient
Monotonic stack, Just remember, we cannot pop blindly to protect monotonic property
IF the char has no freq left, means we will not see that in future, i cannot pop that to protect the property
Also skip if an element already present
'''
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        current = set()
        for i in range(len(s)):
            if s[i] in current:
                freq[s[i]] -= 1
                continue
            while stack and  stack[-1] > s[i] and freq[stack[-1]] > 0:
                current.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            current.add(s[i])
            freq[s[i]] -= 1
        return "".join(stack)
# Time: O(n), initial code didn't have a separate tracker stack, which made it polynomial
# Space: O(n)