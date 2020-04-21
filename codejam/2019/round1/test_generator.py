import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter
import random

def generate_test_cases(n):
	letters = "AB"
	res = set()
	print(1)
	print(n)
	for i in range(n):
		while True:
			count = random.randint(1,6)
			temp = random.choices(letters, k=count)
			temp = "".join(temp)
			if temp not in res:
				res.add(temp)
				break
	[print(x) for x in res]


def main():
    generate_test_cases(6)


if __name__=="__main__":
	main()