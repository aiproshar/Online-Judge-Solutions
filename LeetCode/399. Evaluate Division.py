class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = defaultdict(list)

        for i in range(len(equations)):
            x, y = equations[i]
            cost = values[i]
            adj_list[x].append((cost, y))
            adj_list[y].append(((1.00 / float(cost)), x))

        def bfs(source) -> dict:
            costs = {source: 1}
            que = deque([source])

            while que:
                current = que.popleft()
                for cost, child in adj_list[current]:
                    if child not in costs:
                        '''
                        a/b * b/c = a/c thats the whole idea here
                        '''
                        costs[child] = costs[current] * float(cost)
                        que.append(child)
            return costs

        divs = {}

        for source in adj_list.keys():
            costs = bfs(source)
            for dest, value in costs.items():
                divs[(source, dest)] = value
        res = []
        for x, y in queries:
            if (x, y) in divs:
                res.append(divs[(x, y)])
            else:
                res.append(-1.00000)
        return res

# Time Complexity: O( V(V+ E) + Q) where Q = len(queries)
# Space Complexity: O(V^2)



