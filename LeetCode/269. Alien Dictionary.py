"""
Hard Variant Topo Sort
Used khans algorithm
Also we need to validate the input is correct, the input can be contradictory
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj_list = defaultdict(set)
        indegree = {}
        for word in words:
            for ch in word:
                indegree[ch] = 0
        for k in range(len(words) - 1):
            for i in range(min(len(words[k]), len(words[k + 1]))):
                if words[k][i] != words[k + 1][i]:
                    if words[k + 1][i] not in adj_list[words[k][i]]:
                        adj_list[words[k][i]].add(words[k + 1][i])
                        indegree[words[k + 1][i]] += 1
                    break
            else:
                # First check, if one word is prefix of another, prefix must come before
                if len(words[k]) > len(words[k + 1]):
                    return ""

        que = deque([x for x in indegree.keys() if indegree[x] == 0])
        res = []
        while que:
            current = que.popleft()
            res.append(current)
            for child in adj_list[current]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    que.append(child)

        # second check, it's not a DAG
        # Not DAG means input data contradictory to each other
        # If there is a cycle we won't be able to pop all nodes
        if len(res) < len(indegree):
            return ""
        return "".join(res)

# Time Complexity: O(n*L), L = avg word length. As bounded, its a O(C)
# Space: O(26 * 26) -> O(1)