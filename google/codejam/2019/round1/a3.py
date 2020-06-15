import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter
import random

def test_case():
	r, c = list(map(int, input().split()))
	g = [[0 for i in range(r*c)] for i in range(r*c)]
	for i in range(r*c):
		for j in range(r*c):
			x1 = i // c
			y1 = i % c
			x2 = j // c
			y2 = j % c
			if x1 != x2 and y1 != y2 and x1 - x2 != y1 - y2 and x1 - x2 != y2 - y1:
				g[i][j] = 1
	times = 0

	while times < 100:
		times += 1
		res = list(range(r*c))
		random.shuffle(res)
		for i in range(r*c - 1):
			for k in range(i+1, r*c):
				if g[res[i]][res[k]] == 1:
					res[i+1], res[k] = res[k], res[i+1]
					break
			else:
				break
		else:
			print("POSSIBLE")
			for x in res:
				print(x // c + 1, x % c + 1)
			break
	else:
		print("IMPOSSIBLE")

def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()