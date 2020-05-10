import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter


def find(x, counter, n):
	res = 0
	if counter[x] >= n:
		return res
	n -= counter[x]
	temp = 0
	while x <= 10 ** 9 and n > 0:
		x *= temp
		if counter[x] 
		res += counter[x]
		n 
		if counter[x]


def test_case():
	n, d = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	q = []
	counter = Counter(arr)
	res = 0
	for i in range(n):
		heapq.heappush(q, (counter[arr[i]], arr[i]))




def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()