import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter
import random

def test_case(f):
	vase = [0] * 21
	j = 1
	for i in range(1, 60):
		n = int(input())
		if j > 15: j = 1
		print(j, 1)
		j += 1
		print("n is : {}\n".format(n), file=f, flush=True)
		
	cur = 1
	for i in range(60, 80):
		n = int(input())
		print(cur, 0, flush=True)
		print("n is : {}\n".format(n), file=f, flush=True)
		temp = list(map(int, input().split()))
		vase[cur] = int(temp[0])
		cur += 1
	
	q = []
	for i in range(1, 21):
		heapq.heappush(q, (vase[i], i))
	resnum, residx = heapq.heappop(q)

	print(vase, resnum, residx, q, file=f, flush=True)

	for i in range(80, 100):
		n = int(input())
		print("n is : {}\n".format(n), file=f, flush=True)
		num, idx = heapq.heappop(q)
		heapq.heappush(q, (num+1, idx))
		print(idx, num+1, flush=True)
		# temp = list(map(int, input().split()))

	n = int(input())
	print("n is : {}\n".format(n), file=f, flush=True)
	print(residx, 100, flush=True)


def main():
    T = int(input())
    
    for i in range(1, T+1):
        # print("Case #{}: ".format(i), end = "")
        with open('debug.txt', 'w') as file:
	        test_case(file)

if __name__=="__main__":
	main()

