import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def test_case():
	x, y = list(map(int, input().split()))
	posx = 0
	negx = 0
	posy = 0
	negy = 0
	bound = 2 ** (math.ceil(math.sqrt(max(abs(x), abs(y)))) + 1) - 1
	for posx in range(1, bound):
		negx = posx - x
		if posx & negx != 0: 
			continue
		ysum = bound - (negx + posx)
		if (ysum - y) % 2 != 0:
			continue
		a = (ysum - y) // 2
		posy = a + y
		negy = a
		if posy ^ negy ^ posx ^ negx == bound:
			i = 1
			res = ""
			print('bound {0:07b}, {1:07b}, {2:07b}, {3:07b}, {4:07b}'.format(bound, posx, negx, posy, negy))
			while i < bound + 1:
				if i & posx != 0:
					res += "E"
				elif i & negx != 0:
					res += "W"
				elif i & posy != 0:
					res += "N"
				elif i & negy != 0:
					res += "S"
				i = i << 1
			print(res)
			return 
		else:
			continue
	print("IMPOSSIBLE")


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()