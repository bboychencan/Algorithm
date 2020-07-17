import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	# n, a, b = int(input())
	# arr = list(map(int, input().split()))
	# layers = [0 for i in range(n + 1)]
	# layers[0] = 1
	# dic = {}
	# dic[1] = 0
	# for i in range(n):
	# 	par = arr[i]
	# 	dic[i+2] = dic[par] + 1
	# 	layers[dic[i+2]] += 1

	# total = 0

	# for i in range(a):
	# 	# count = 0
	# 	l = i
	# 	pos = 1
	# 	while layers[l] > 0:
	# 		total += layers[l] * pos
	# 		l += a
	# 		pos += 1

	# for i in range(b):
	# 	# count = 0
	# 	l = i
	# 	pos = 1
	# 	while layers[l] > 0:
	# 		total += layers[l] * pos
	# 		l += b
	# 		pos += 1

	# # print(total / (n + 1))

	pass


	
def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

