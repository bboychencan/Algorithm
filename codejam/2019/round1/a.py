import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter


def dfs(cnt, u):

def test_case():
	
	r, c = list(map(int, input().spilt))
	g = [[[] for i in range(c)] for i in range(r)]
	for i in range(r):
		for j in range(c):
			for ii in range(r):
				for jj in range(c):
					if(i !+ ii and j != jj and i - j != ii - jj and i + j != ii + jj):
						g[i*c + j].append(ii * w + jj)



def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()