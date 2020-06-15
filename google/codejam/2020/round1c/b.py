import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def test_case():
	u = int(input())
	MAX = 10 ** 4
	q = [0] * (MAX)
	r = [0] * (MAX)
	res = [0] * 10
	counter = defaultdict(int)
	letters = set()

	for i in range(MAX):
		q[i], r[i] = list(input().split())
		if len(letters) != 10: 
			letters |= set(r[i])
		counter[r[i][0]] += 1

	temp = sorted(counter.items(), key=lambda x: - x[1])
	for i in range(1, 10):
		res[i] = temp[i-1][0]
	res[0] = list((letters - set(res[1:10])))[0]
	print("".join(res))


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()