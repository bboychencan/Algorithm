import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	n, a, b = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	arr = [0, 0] + arr

	count = 0
	

	def find_par(node, x):
		res = 0
		while x > 0 and node > 0:
			node = arr[node]
			x -= 1

		return node

	for i in range(1, n + 1):
		for j in range(1, n + 1):
			vis = [0 for i in range(n + 1)]
			temp = 0
			node = i
			while node > 0:
				vis[node] = 1
				temp += 1
				node = find_par(node, a)
			node = j
			while node > 0:
				if vis[node] != 1:
					temp += 1
				node = find_par(node, b)
			count += temp

	print(count / (n ** 2))



def main():
	T = int(input())
	for i in range(1, T+1):
		print("Case #{}: ".format(i), end = "")
		test_case()


if __name__=="__main__":
	main()

