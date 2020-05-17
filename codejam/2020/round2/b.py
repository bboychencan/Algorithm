import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random
import heapq

def test_case():
	c, d = list(map(int, input().split()))
	edges = [0 for i in range(d)]
	edge_map = {}
	graph = [[] for i in range(c+1)]
	status = list(map(int, input().split()))
	timestamp = [1001] * (c + 1)
	timestamp[1] = 0
	qtimes = []
	qranks = []
	vis = [0] * (c + 1)
	vis[1] = 1

	for i in range(2, c+1):
		x = status[i-2]
		if x < 0:
			qranks.append([-x, i])
		else:
			qtimes.append([x, i])

	heapq.heapify(qtimes)
	heapq.heapify(qranks)

	for i in range(d):
		u, v = list(map(int, input().split()))
		edges[i] = (u, v)
		edge_map[(min(u,v), max(u, v))] = 1000
		graph[u].append(v)
		graph[v].append(u)

	count = 1
	t = 0

	# print(qtimes, qranks, graph)

	while qtimes and qranks:
		# print(qranks[0][0], count)
		if qranks[0][0] < count:
			rank, idx = heapq.heappop(qranks)
			ok = False
			for i in graph[idx]:
				if timestamp[i] != 1001:
					mini, maxi = min(idx, i), max(idx, i)
					if not ok:
						edge_map[(mini, maxi)] = t - timestamp[i]
						timestamp[idx] = t
						ok = True
					else:
						edge_map[(mini, maxi)] = 1000
			count += 1

		elif qranks[0][0] == count:
			rank, idx = heapq.heappop(qranks)
			ok = False
			for i in graph[idx]:
				if timestamp[i] != 1001:
					mini, maxi = min(idx, i), max(idx, i)
					if not ok:
						t += 1
						edge_map[(mini, maxi)] = t - timestamp[i]
						timestamp[idx] = t
						ok = True
					else:
						edge_map[(mini, maxi)] = 1000
			count += 1

		else:
			while qranks[0][0] > count:
				temp, idx = heapq.heappop(qtimes)
				ok = False
				for i in graph[idx]:
					mini, maxi = min(idx, i), max(idx, i)
					if not ok:
						t = temp
						edge_map[(mini, maxi)] = t - timestamp[i]
						timestamp[idx] = t
						ok = True
					else:
						edge_map[(mini, maxi)] = 1000
				count += 1
	while qtimes:
		temp, idx = heapq.heappop(qtimes)
		ok = False
		for i in graph[idx]:
			mini, maxi = min(idx, i), max(idx, i)
			if not ok:
				t = temp
				edge_map[(mini, maxi)] = t - timestamp[i]
				timestamp[idx] = t
				ok = True
			else:
				edge_map[(mini, maxi)] = 1000
		count += 1

	while qranks:
		# rank, idx = heapq.heappop(qranks)
		# ok = False
		# # print(rank, idx, graph[idx])
		# for i in graph[idx]:
		# 	# print('timestamp', timestamp[i], t)
		# 	if timestamp[i] != 1001:
		# 		mini, maxi = min(idx, i), max(idx, i)
		# 		if not ok:
		# 			t += 1
		# 			edge_map[(mini, maxi)] = t - timestamp[i]
		# 			timestamp[idx] = t
		# 			# print('here', idx, i)
		# 		else:
		# 			edge_map[(mini, maxi)] = 1000
		# count += 1


		if qranks[0][0] < count:
			rank, idx = heapq.heappop(qranks)
			ok = False
			for i in graph[idx]:
				if timestamp[i] != 1001:
					mini, maxi = min(idx, i), max(idx, i)
					if not ok:
						edge_map[(mini, maxi)] = t - timestamp[i]
						timestamp[idx] = t
						ok = True
					else:
						edge_map[(mini, maxi)] = 1000
			count += 1

		elif qranks[0][0] == count:
			rank, idx = heapq.heappop(qranks)
			ok = False

			for i in graph[idx]:
				if timestamp[i] != 1001:
					# print(i, idx)
					mini, maxi = min(idx, i), max(idx, i)
					if not ok:
						t += 1
						edge_map[(mini, maxi)] = t - timestamp[i]
						timestamp[idx] = t
						ok = True
					else:
						edge_map[(mini, maxi)] = 1000
			count += 1

	# res = []
	# print('edge map', edge_map)
	for i in range(d):
		print("{}".format(edge_map[edges[i]]), end=" ")
	# print("\n")


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()
        print("")


if __name__=="__main__":
	main()

