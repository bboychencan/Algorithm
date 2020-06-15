import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

N = 0
M = 0


def ext_eucli(a, b, c):
	if b == 1:

def crt(a, r):



def test_case():
	spades = [5, 7, 9, 11, 13, 16, 17]
	r = [0 for i in range(7)]
	count = 10

	for i in range(len(spades)):
		print(" ".join(list(map(str, [spades[i] for j in range(18)]))), flush=True)
		holes = list(map(int, input().split()))
		r[i] = sum(holes) % spades[i]

	for i in range(1, 1000001):
		for j in range(7):
			if i % spades[j] != r[j]: 
				break
		else:
			count = i
			break

	print('{}'.format(count), flush=True)
	res = int(input())
	if res == -1:
		return False
	else:
		return True

def main():
	global N, M
	T, N, M = list(map(int, input().split()))
	for i in range(1, T + 1):
		res = test_case()
		if not res:
			break

if __name__=="__main__":
	main()