import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	n, k, p = list(map(int, input().split()))
	arr = [None for i in range(n)]
	for i in range(n):
		arr[i] = list(map(int ,input().split()))

	dp = [-1] * (p + 1)
	dp[0] = 0

	res = 0
	for i in range(n):
		for j in range(p, 0, -1):
			temp = 0
			for l in range(1, min(j, k) + 1):
				temp += arr[i][l - 1]
				if dp[j - l] == -1:
					continue
				else:
					dp[j] =	max(dp[j], dp[j - l] + temp)
	print(dp[p])


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

