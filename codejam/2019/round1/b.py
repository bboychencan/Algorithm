import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

N = 0
M = 0

def test_case():
	holes = [0] * 18
	spades = [3] * 18
	count = 10
	for i in range(N):
		print(" ".join(list(map(str, spades))), flush=True)
		holes = list(map(int, input().split()))
	print('{}'.format(count), flush=True)
	res = int(input())
	if res == -1:
		return False

def main():
	global N, M
	T, N, M = list(map(int, input().split()))
	for i in range(1, T + 1):
		res =test_case()
		if not res:
			break

if __name__=="__main__":
	main()