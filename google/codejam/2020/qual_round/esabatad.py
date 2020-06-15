T, B = list(map(int, input().split()))


for x in range(1, T + 1):
	bits = [''] * B
	answer = None
	for i in range(1, B + 1):
		print(i)
		s = input()
		bits[i-1] = s
	res = "".join(bits)
	print(res[::-1])
	answer = input()
	if answer == "N": break
