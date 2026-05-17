# Typical monotonic stack problem
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [((target - p) / s, p) for p, s in zip(position, speed)]

        time.sort(key=lambda x: x[1])
        time = [x[0] for x in time]

        stack = []
        fleets = 0

        for x in time:
            while stack and x >= stack[-1]:
                stack.pop()
            stack.append(x)
        return len(stack)

# Time complexity: O(nlgn) -> sort
# Space Complexity: O(n)