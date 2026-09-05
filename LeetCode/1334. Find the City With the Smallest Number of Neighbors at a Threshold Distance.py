'''
Base case floyd Warshall algorithm
Constraints allows use to use FW
'''
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        distance = [[math.inf] * n for _ in range(n)]

        for i in range(n):
            distance[i][i] = 0

        for x, y, cost in edges:
            # corner case, instead of directly assigning, there can de duplicate edges for same pair
            # we cannot do blind set in that scenario, must store the best cost
            distance[x][y] = min(distance[x][y], cost)
            distance[y][x] = min(distance[y][x], cost)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        valid_cities = []
        for i in range(n):
            reachable = 0
            for j in range(n):
                if i == j:
                    continue
                if distance[i][j] <= distanceThreshold:
                    reachable += 1
            valid_cities.append([reachable, i])
        valid_cities.sort(key=lambda x: (x[0], -x[1]))

        return valid_cities[0][1]

# Time Complexity: O(n^3)
# Space Complexity: O(n^2)