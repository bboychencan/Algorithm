
T = int(input())
for x in range(T):
	n, t = list(map(int, input().split()))
	a = list(map(int, input().split()))
	a = sorted(a)
	res = 0

	dp = [0] * (t + 1)
	dp[0] = 1
	for i in range(n):
		for j in range(t-1, a[i] - 1, -1):
			if dp[j] == 1:
				res = max(res, a[i] + j)
			else:
				dp[j] = dp[j-a[i]] 

	print(res)