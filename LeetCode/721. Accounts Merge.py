'''
Disconnected Graph based advanced variant, find each connected graph and all node group
'''


class Solution:
    def _bfs(self, source, adj_list, visited) -> list[str]:

        que = deque()
        que.append(source)
        visited.add(source)
        explored = [source]
        while que:
            current = que.popleft()
            for child in adj_list[current]:
                if child not in visited:
                    visited.add(child)
                    explored.append(child)
                    que.append(child)
        return sorted(explored)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        adj_list = defaultdict(list)
        # key=email -> value: name
        email_name = {}
        visited = set()
        for name, *emails in accounts:
            email_name[emails[0]] = name
            for i in range(len(emails) - 1):
                adj_list[emails[i]].append(emails[i + 1])
                adj_list[emails[i + 1]].append(emails[i])
                email_name[emails[i + 1]] = name

        res = []
        for email in email_name.keys():
            if email in visited:
                continue
            account = [email_name[email]]
            account.extend(self._bfs(email, adj_list, visited))
            res.append(account)
        return res

# V -> unique emails; N -> total email occurrences across accounts (N >= V)
# E -> No of edges, can go to V^2 is fully connected graph. But the way we construct lean tree its ~ O(V)
# L -> max email length; string hash/compare is O(L), not O(1)
#
# Adjacency build: O(N·L)      -- N hash inserts
# BFS (all comps): O((V+E)·L)  = O(N·L)
# Sorting:         O(V·L·log V) -- sum(c_i log c_i) <= V log V comparisons, O(L) each
#
# Overall: O(N·L + V·L·log V)  ->  O(N·L·log N)
# Space:   O(N·L) for stored strings + O(V+E) = O(N) references


'''
DSU based implementation YaY
'''

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        root = {}
        names = {}

        def find(node):
            # not present
            if node not in root:
                root[node] = node
                return node
            if root[node] != node:
                root[node] = find(root[node])
            return root[node]

        def union(n1, n2) -> bool:
            r1 = find(n1)
            r2 = find(n2)
            if r1 == r2:
                return False
            root[r1] = r2
            return True

        for name, *emails in accounts:
            names[emails[0]] = name
            # side effect so email is in the root dict
            find(emails[0])
            for i in range(1, len(emails)):
                union(emails[0], emails[i])
                names[emails[i]] = name

        unions = defaultdict(list)
        for node in root.keys():
            # path compression
            unions[find(node)].append(node)
        res = []
        for email in unions.keys():
            temp = [names[email]]
            temp.extend(sorted(unions[email]))
            res.append(temp)

        return res

# Time Complexity: 