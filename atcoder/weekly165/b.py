x = int(input())

year = 0
cur = 100

while cur < x:
	year += 1
	cur = int(cur * 1.01)

print(year)