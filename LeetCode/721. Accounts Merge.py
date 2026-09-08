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