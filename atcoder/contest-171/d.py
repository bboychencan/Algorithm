from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
q = int(input())

counter = Counter(arr)
total = sum(arr)

for i in range(q):
	b, c = list(map(int, input().split()))
	if counter[b] > 0:
		counter[c] += counter[b]
		total += counter[b] * (c - b)
		counter[b] = 0
		print(total)
	else:
		print(total)
