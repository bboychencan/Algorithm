import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter
import random

def test_case():
	h, w = list(map(int, input().split()))
	g = [[] for i in range(h*w)]
	for i in range(h):
		for j in range(w):
			for ii in range(h):
				for jj in range(w):
					if i != ii and j != jj and i-j != ii-jj and i+j != ii+jj:
						g[i*w + j].append(ii*w + jj)
			random.shuffle(g[i*w + j])
	res = None
	cur = []
	visited = [0 for i in range(h*w)]

	def dfs(count, u):
		nonlocal res
		if res: return
		cur.append(u)
		visited[u] = 1
		if count == h * w:
			res = cur[::]
			return
		for v in g[u]:
			if visited[v] == 0:
				dfs(count + 1, v)
		visited[u] = 0
		cur.pop()

	# [print(x) for x in g]
	for i in range(h*w):
		if res: break
		dfs(1, i)
	if not res:
		print("IMPOSSIBLE")
	else:
		print("POSSIBLE")
		for i in res:
			print(i // w + 1, i % w + 1)


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()

if __name__=="__main__":
	main()
