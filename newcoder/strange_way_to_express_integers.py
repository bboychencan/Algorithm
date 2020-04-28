n = int(input())
a = [0 for i in range(n)]
m = [0 for i in range(n)]

for i in range(n):
	m[i], a[i] = list(map(int, input().split()))

def extgcd(x, y):
	if y == 0:
		return 1, 0, x
	old_r, r = x, y
	old_s, s = 1, 0
	old_t, t = 0, 1

	while r:
		q = old_r // r
		old_r, r = r, old_r - q * r
		old_s, s = s, old_s - q * s
		old_t, t = t, old_t - q * t

	return old_s, old_t, old_r

total = 1
for i in range(n):
	total *= m[i]

res = 0

for i in range(n):
	temp = total // m[i]
	s,t,r = extgcd(temp, m[i])
	print(temp, m[i], s, t, r)
	if r != 1:
		res == -1
		break
	s = (s + m[i]) % m[i]
	res += (s * temp * a[i])

if res == -1:
	print(res)
else:
	print(res % total)