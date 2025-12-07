# FucK UVA anyways, too much add in site feels like a spam. AI can develop 20X site, and free version will do so
# CRAP will go back to LC anyways, just following my old graph grinding doc

# BFS, instead of depth calculation we color our childs
# For any tree this will always be bi-colorable
# When we insert a loop, means we find a child which was previously visited, we make sure theres no conflict
# If so then return false

import sys
from collections import deque, defaultdict


def bfs(adj_list : defaultdict, n) -> bool:
	color = [-1] * n
	parent = [None] * n

	queue = deque()

	queue.append(0)
	color[0] = 0
	parent[0] = None

	while queue:
		parent = queue.popleft()
		for child in adj_list[parent]:
			if color[child] == -1:
				if color[parent] == 1:
					color[child] = 0
				else:
					color[child] = 1
				queue.append(child)
			else:
				if color[child] == color[parent]:
					return False
	return True

if __name__ == '__main__':

	while nodes := input():
		nodes = int(nodes)
		if nodes == 0:
			sys.exit(0)
		edges = int(input())
		adj_list = defaultdict(list)
		for _ in range(edges):
			x, y = input().split()
			x = int(x)
			y = int(y)
			adj_list[x].append(y)
			adj_list[y].append(x)

		value = bfs(adj_list, nodes)
		if value:
			print("BICOLORABLE.")
		else:
			print("NOT BICOLORABLE.")