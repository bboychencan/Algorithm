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
	arr = list(map(int, input().split()))

	cur = 0
	res = 0

	while cur + 1 < n:
		icount = 1
		while cur + 1 < n and arr[cur+1] >= arr[cur]:
			if arr[cur+1] > arr[cur]:
				icount += 1
			cur += 1
		res += ((icount - 1) // 4)

		dcount = 1
		while cur + 1 < n and arr[cur+1] <= arr[cur]:
			if arr[cur+1] < arr[cur]:
				dcount += 1
			cur += 1
		res += ((dcount - 1) // 4)

	print(res)



def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()

