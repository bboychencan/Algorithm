import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	r, c = list(map(int, input().split()))
	mat = ["" for i in range(r)]
	vis = [[0 for i in range(c)] for i in range(r)]
	dirs = [[0,1],[0,-1],[-1,0]]
	res = []
	ok = True
	for i in range(r):
		mat[i] = input()
	pominos = set()

	def flood(i, j, x):
		vis[i][j] = 0
		for dx, dy in dirs:
			if 0 <= i + dx < r and 0 <= j + dy < c and \
				vis[i+dx][j+dy] == 1 and mat[i+dx][j+dy] == x: 
				flood(i+dx, j+dy, x)
		# vis[i][j] = 0

	def dfs(i, j, x):
		# print('dfs', i, j, x)
		# [print(line) for line in vis]
		if i + 1 < r and vis[i+1][j] == 0:
			# print('error')
			return False
		else:
			vis[i][j] = 1
			ok = True
			for dx, dy in dirs:
				if 0 <= i + dx < r and 0 <= j + dy < c and \
					vis[i+dx][j+dy] == 0 and mat[i+dx][j+dy] == x: 
					if not dfs(i+dx, j+dy, x):
						ok = False
						break
			# vis[i][j] = 0
			return ok


	for i in range(r-1, -1, -1):
		if not ok: break
		candis = set()
		temp = set()
		for j in range(c):
			if mat[i][j] in pominos or mat[i][j] in temp:
				continue
			else:
				candis.add((j, mat[i][j]))
				temp.add(mat[i][j])
		# print(candis, temp)
		while candis:
			if not ok: 
				break
			for j, v in candis.copy():
				if dfs(i, j, v):
					# print(i,j,v)
					pominos.add(v)
					res.append(v)
					candis.remove((j,v))
					break
				else:
					flood(i,j, v)
			else:
				ok = False
		if candis:
			ok = False

	if not ok:
		print(-1)
	else:
		print("".join(res))




def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

