import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
	N, Q = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	arr = [float('inf')] + arr + [float('inf')]

	querys = []
	querys2 = defaultdict(list)
	for i in range(Q):
		temp = list(map(int, input().split()))
		querys.append(temp)
		querys2[temp[0]].append(temp[1])
  
	res = []
	matrix = defaultdict(dict)
    
	for i in querys2.keys():
		matrix[i][1] = i
		leftdoor = i - 1
		rightdoor = i
		room = i
		steps = set(querys2[i])
		for j in range(2, N + 1):	
			# print(arr[leftdoor], arr[rightdoor])
			if arr[leftdoor] < arr[rightdoor]:
				leftroom = leftdoor
				room = leftroom
				leftdoor -= 1
			elif arr[leftdoor] > arr[rightdoor]:
				rightroom = rightdoor + 1
				room = rightroom
				rightdoor += 1
			if j in steps:
				matrix[i][j] = room
			# print('room, ', room)
	for s, k in querys:
		res.append(matrix[s][k])

	print(*res)

def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()