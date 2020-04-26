import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def fast_power(k, n):
    a = 10 % n
    res = 1
    while k > 0:
        if k & 1 == 1:
            res = res * a % n
        a = a * a % n
        k = k >> 1
    return res
    
    
def test_case():
    n, m, k, x = list(map(int, input().split()))
    res = 0
    res = (x + fast_power(k, n) * m % n) % n
    print(res)


def main():
    test_case()


if __name__=="__main__":
	main()