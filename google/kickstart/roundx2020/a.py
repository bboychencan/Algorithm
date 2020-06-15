import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from collections import Counter
import random

def test_case():
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    res = 0
    cur = 0
    while cur < n:
        if nums[cur] != k:
            cur += 1
            continue
        else:
            # print(nums[cur], k)
            temp = k
            while cur < n and temp > 0 and nums[cur] == temp:
                cur += 1
                temp -= 1
            if temp == 0:
                res += 1
    print(res)

def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
    main()

