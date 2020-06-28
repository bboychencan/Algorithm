n = int(input())

arr = list(map(int, input().split()))

all_xor = arr[0]

for i in range(1, n):
	all_xor ^= arr[i]

res = [0 for i in range(n)]

for i in range(n):
	res[i] = all_xor ^ arr[i]

print(" ".join(list(map(str, res))))