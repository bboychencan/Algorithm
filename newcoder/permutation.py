n = int(input())

MAX = 2 ** n
for i in range(MAX):
	temp = []
	j = 1
	count = 1
	while count <= n:
		# print(bin(i), bin(j))
		if j & i != 0:
			temp.append(count)
		j = j << 1
		count += 1
	# print(*temp)
	print(*temp)
