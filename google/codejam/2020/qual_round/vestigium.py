T = int(input())

for x in range(1, T + 1):
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    
    trace = 0
    r = 0
    c = 0
    for i in range(n):
        trace += mat[i][i]
    for i in range(n):
        row = mat[i]
        row = set(row)
        if len(row) < n: 
            r += 1
    for i in range(n):
        col = [mat[j][i] for j in range(n)]
        col = set(col)
        if len(col) < n:
            c += 1
    print("Case #{}: {} {} {}".format(x,trace,r,c))
    