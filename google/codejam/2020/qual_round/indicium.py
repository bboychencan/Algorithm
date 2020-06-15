from itertools import combinations
from itertools import permutations

T = int(input())
for x in range(1, T+1):
    n, k = list(map(int, input().split()))
    # print(n, k)
    digits = [str(i) for i in range(1, n+1)]
    perm = list(permutations(digits))
    combs = list(permutations(perm, n))

    poss = False
    for comb in combs:
        for j in range(n):
            col = set()
            for i in range(n):
                col.add(comb[i][j])
            if len(col) != n: 
                break
        else:
            # print('here', n, k)
            # print(comb)
            trace = 0
            for i in range(n):
                trace += int(comb[i][i])
            # print(trace, k)
            if trace == k:
                poss = True
                print("Case #{}: {}".format(x, "POSSIBLE"))
                for i in range(len(comb)):
                    print(" ".join(list(map(str, comb[i]))))
                break
    if not poss:
        print("Case #{}: {}".format(x, "IMPOSSIBLE"))
