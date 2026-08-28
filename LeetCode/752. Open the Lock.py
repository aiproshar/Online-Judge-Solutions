class Solution:
    def _childs(self, parent: str) -> list[str]:
        # 8 neighbours
        res = []
        parent = list(parent)
        parent = [int(x) for x in parent]
        for i in range(len(parent)):
            # increment
            temp = parent.copy()
            temp[i] = (temp[i] + 1) % 10
            temp = [str(x) for x in temp]
            res.append("".join(temp))

            # decrement
            temp = parent.copy()
            temp[i] = (temp[i] - 1) % 10
            temp = [str(x) for x in temp]
            res.append("".join(temp))
        return res

    def openLock(self, deadends: List[str], target: str) -> int:

        source = "0000"
        deadends = set(deadends)

        # Edge Case 01: source in deadend, means we doomed
        if source in deadends:
            return -1
        # Edge Case 02: Target is source, we need 0 tries
        if target == source:
            return 0

        # General Case
        depth = {source: 0}

        que = deque([source])
        while que:
            parent = que.popleft()
            childs = self._childs(parent)
            for child in childs:
                if child not in depth and child not in deadends:
                    depth[child] = depth[parent] + 1
                    que.append(child)
                    # early termination
                    if child == target:
                        return depth[child]

        return -1

# Time Complexity: O(V+E) O(10^4) total verteices
# Space Complexity: O(V), 10^4