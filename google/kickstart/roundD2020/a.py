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
	res = 0
	arr = list(map(int, input().split()))
	bm = arr[0]
	premax = -float('inf')

	for i in range(len(arr)):
		if arr[i] > premax:
			if i == len(arr) - 1 or arr[i] > arr[i+1]:
				res += 1
			premax = arr[i]

	print(res)


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

