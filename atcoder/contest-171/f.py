from itertools import combinations

k = int(input())
s = list(input())

tags = [set() for i in range(k + len(s))]

res = 0


for x in combinations(range(k + len(s)), len(s)):
	opts = set(range(k + len(s))) - set(x)
	# for idx in x:
	temp = 1
	for idx in opts:
		if 26 - len(tags[idx]) == 0:
			continue
		else:
			temp = (temp * (26 - len(tags[idx]))) % (10 ** 9 + 7)
	if temp == 1:
		break
	res = (res + temp) % (10 ** 9 + 7)
	for i, idx in enumerate(x):
		tags[idx].add(s[i])

print(res)
