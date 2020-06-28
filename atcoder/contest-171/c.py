n = int(input())

n = n - 1

root = 26
p = 1


while n >= root:
	n -= root
	root *= 26
	p += 1


res = ['a'] * p

while n > 0:
	r = n % 26
	res[p - 1] = chr(ord('a') + r)
	n = n // 26
	p -= 1

print(''.join(res))