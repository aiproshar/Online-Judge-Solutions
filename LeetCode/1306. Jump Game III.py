'''
Basic BFS problem YaY too EZ

Memoization to mark if a node is visited or not (yeah saves us from infinite loop too)
First check if our jumps positions are valid or not, push the valid jump positions if they are not visited
Oww - Check first for objective, our value in that index is 0 or not
If we encounter any 0, break and return true, else false
'''


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        visited = set()

        que = deque()
        que.append(start)
        visited.add(start)

        while que:
            current = que.popleft()
            if arr[current] == 0:
                return True
            right_jump = current + arr[current]
            left_jump = current - arr[current]

            if left_jump in range(len(arr)) and left_jump not in visited:
                visited.add(left_jump)
                que.append(left_jump)
            if right_jump in range(len(arr)) and right_jump not in visited:
                visited.add(right_jump)
                que.append(right_jump)
        return False
