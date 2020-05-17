import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	L, R = list(map(int, input().split()))
	l = L
	r = R
	cur = 1
	n = 0
	while l >= cur or r >= cur:
		if l >= r:
			l -= cur
		else:
			r -= cur
		cur += 1
		n += 1
	print(n, l, r)

def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

