import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def test_case():
	n = int(input())
	patterns = []
	for i in range(n):
		patterns.append(input().split("*"))
		# print(patterns)

	start = ""
	end = ""
	res = ""
	for i in range(n):
		if len(patterns[i][0]) > len(start):
			start = patterns[i][0]
		if len(patterns[i][-1]) > len(end):
			end = patterns[i][-1]

	for i in range(n):
		if not start.startswith(patterns[i][0]):
			res = "*"
			break
		if not end.endswith(patterns[i][-1]):
			res = "*"
			break
	if res != "*":
		temp = ""
		for i in range(n):
			temp += "".join(patterns[i][1:-1])
		res = start + temp + end
	print(res)


def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()