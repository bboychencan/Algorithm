import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def test_case():
	x, y, m = list(input().split())
	x = int(x)
	y = int(y)
	n = len(m)
	d = [0] * (n + 1)
	d[0] = abs(x) + abs(y)
	c1 = x
	c2 = y
	for i in range(n):
		if m[i] == 'S':
			c2 -= 1
		elif m[i] == 'N':
			c2 += 1
		elif m[i] == 'W':
			c1 -= 1
		elif m[i] == 'E':
			c1 += 1
		d[i+1] = abs(c1) + abs(c2)



	res = -1
	for i in range(n+1):
		if d[i] <= i:
			res = i
			break

	if res != -1:
		print(res)
	else:
		print("IMPOSSIBLE")


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()