import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	n = int(input())
	points = [None] * n
	for i in range(n):
		points[i] = list(map(int, input().split()))

	res = 0
	for i in range(n):
		for j in range(n):
			balls = set()
			if i != j:
				dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
				for a, b in combinations(range(n), 2):
					dx2, dy2 = points[b][0] - points[a][0], points[b][1] - points[a][1]
					if dy * dx2 == dy2 * dx:
						balls.add(a)
						balls.add(b)
			if len(balls) < n - 1:
				res = max(res, len(balls) + 2)
			elif len(balls) < n:
				res = max(res, len(balls) + 1)
			else:
				res = max(res, len(balls))
				# print(i, j, balls)
	print(res)

def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

