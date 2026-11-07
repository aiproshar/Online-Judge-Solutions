class Solution:
    def canRemoveAll(
        self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        stack = []
        for i in range(len(types)):
            current = types[i]
            color = colors[i]
            if stack and stack[-1][0] == current and stack[-1][1] == color:
                stack[-1][2] += 1
            else:
                stack.append([current, color, 1])
            if groupSize[current] == stack[-1][2]:
                stack.pop()

        return stack == []

# Time Complexity: O(n)
# Space Complexity: O(n)