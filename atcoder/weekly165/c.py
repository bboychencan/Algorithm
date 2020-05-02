n, m, q = list(map(int, input().split()))

arr = [None] * q
for i in range(q):
	arr[i] = list(map(int, input().split()))

arr = sorted(arr, key=lambda x : (x[0], x[1]))

def dfs(cur, arr, val):
	if cur >= len(arr):
		return 0
	if cur == len(arr) - 1:
		return arr[cur][3]

	nex = val + (arr[cur][1] + 
	for i in range(cur+1, len(arr)):
		if arr[i][0] 

	return max