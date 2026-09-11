'''
Backtracking Brute force Solution
We explore all possible ways, whenever we are able to burn all tickets we store the result
After that we sort them and return the smallest lexical one
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj_list = defaultdict(lambda: defaultdict(int))
        for x, y in tickets:
            adj_list[x][y] += 1

        res = None

        def backtrack(source, current):
            nonlocal res
            if len(current) == len(tickets):
                current.append(source)
                temp = ".".join(current)
                if res is None or temp < res:
                    res = temp
                current.pop()
                return
            current.append(source)
            for dest in adj_list[source].keys():
                if adj_list[source][dest] > 0:
                    adj_list[source][dest] -= 1
                    backtrack(dest, current)
                    adj_list[source][dest] += 1
            current.pop()

        backtrack("JFK", [])
        return res.split('.')

# Time Complexity: We have V choices (for a dense graph) and We must pick one from E and E is depth, so V ^ E.
# Also can be E! because first we have E tickets then E-1, E-2, ..... and this is upper bound
# Space Complexirt: O(E) recursion depth, O(E) adj list
'''
Greedy + Backtrack 
Instead of looking where we can go, we look where we can go smallest lexically
So the first we return to a leaf edge is our answer, we can skip exploring
Time complexity is still same because maybe we have only onw valid answer and its the lexically largest one
'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj_list = defaultdict(lambda: defaultdict(int))
        for x, y in tickets:
            adj_list[x][y] += 1

        res = None

        def backtrack(source, current):
            nonlocal res
            if res != None:
                return
            if len(current) == len(tickets):
                current.append(source)
                temp = ".".join(current)
                res = temp
                current.pop()
                return
            current.append(source)
            destinations = sorted(adj_list[source].keys())
            for dest in destinations:
                if adj_list[source][dest] > 0:
                    adj_list[source][dest] -= 1
                    backtrack(dest, current)
                    adj_list[source][dest] += 1
            current.pop()

        backtrack("JFK", [])
        return res.split('.')



'''
This is a Eulerian Paths algorithm, we need to create a path which uses all the edges
All graph doesnt not have this property, but this is guaranteed by the problem

Our focus here is the edges AKA the tickets, we keep track of edges we used
We dont give much thoughts about vertex themself

JFK is given as starting point
'''


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_list = defaultdict(deque)
        for x, y in tickets:
            adj_list[x].append(y)
        res = []

        def dfs(src):
            while adj_list[src]:
                dest = adj_list[src].popleft()
                dfs(dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]

# Time Complexity: O(ElogE) for sort, O(E) to build adj_list, DFS goes to O(E) depth
# Space Complexity: O(E)