from itertools import permutations
import copy

rows = None
cols = None
possk = {}


def dfs(board, x, y, n):
    candis = set(range(1, n + 1)) ^ (rows[x] | cols[y])
    
    for i in candis:
        board[x][y] = i
        rows[x].add(i)
        cols[y].add(i)
        if y + 1 < n:
            dfs(board, x, y+1, n)
        elif x + 1 < n:
            dfs(board, x+1, 0, n)
        else:
            temp = 0
            for a in range(n):
                temp += board[a][a]
            possk[(n, temp)] = copy.deepcopy(board)
        board[x][y] = 0
        rows[x].remove(i)
        cols[y].remove(i)
        
    return False

for x in range(2, 6):
    rows = [set() for i in range(x)]
    cols = [set() for i in range(x)]
    mat = [[0 for i in range(x)] for i in range(x)]
    dfs(mat, 0, 0, x)



T = int(input())
for x in range(1, T+1):
    n, k = list(map(int, input().split()))
    poss = False

    if n <= 5:
        if (n, k) in possk:
            print("Case #{}: {}".format(x, "POSSIBLE"))
            for i in range(n):
                print(" ".join(list(map(str, possk[(n,k)][i]))))
            continue
    print("Case #{}: {}".format(x, "IMPOSSIBLE"))