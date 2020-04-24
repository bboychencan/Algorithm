def fast_power(a, n):
	if n == 0: return 1
	res = 1
	while n > 0:
		if n & 1 == 1:
			res *= a
		a = a * a
		n = n >> 1
	return res

def brute_force(a, n):
	res = 1
	for i in range(n):
		res *= a
	return res

if __name__ == '__main__':
	a, n = list(map(int, input().split()))
	res = fast_power(a, n)
	# res = brute_force(a, n)
	print('finish')