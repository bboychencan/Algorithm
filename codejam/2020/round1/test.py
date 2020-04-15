import math

def get_ele(r, k):
	return math.factorial(r - 1) // math.factorial(k - 1) // math.factorial(r-k)

res = 0
while True:
	r, k = list(map(int, input().split()))
	res += get_ele(r, k)
	print(res)