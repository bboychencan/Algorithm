from collections import deque

N, M = list(map(int, input().split()))

paths = [[] for i in range(N+1)]

for i in range(M):
	a, b = list(map(int, input().split()))
	paths[a].append(b)
	paths[b].append(a)

q = deque([1])
vis = set([1])
res = None
count = 0

while q:
	n = len(q)
	res = set(q)
	# print(res)
	for i in range(n):
		top = q.popleft()
		for x in paths[top]:
			if x not in vis:
				q.append(x)
				vis.add(x)
	count += 1

# print(res)
print(min(res), count-1, len(res))

