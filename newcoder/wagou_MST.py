n, m = list(map(int, input().split()))
edges = [0 for i in range(m)]

for i in range(m):
    edges[i] = list(map(int, input().split()))
    
    
parent = [-1 for i in range(n + 1)]

def find(x):
    if parent[x] == -1:
        return x
    parent[x] = find(parent[x])
    return parent[x]

edges = sorted(edges, key = lambda x: x[2])

select = []
res = 0
for i in range(m):
    a, b, w = edges[i]
    x = find(a)
    y = find(b)
    if x == y: continue
    parent[x] = y
    select.append((a, b))
    res += w
    if len(select) == n - 1:
        break

print(res)