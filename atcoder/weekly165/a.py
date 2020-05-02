k = int(input())
a, b = list(map(int, input().split()))

cur = a // k * k

def solve():
	global cur
	while cur <= b:
		if cur >= a:
			print("OK")
			return
		cur += k
	print("NG")

solve()