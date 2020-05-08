n = int(input())

l = [0] * n
r = [0] * n

for i in range(n):
	l[i] = int(input())
for i in range(n):
	r[i] = int(input())

dp = [0] * (n+1)
pre = [0] * (n+1)

for i in range(n-1, -1, -1):
	for j in range(n-1, -1, -1):
		temp = 0
		if abs(l[i] - r[j]) <= 4:
			temp = max(temp, pre[j+1] + 1)
			# temp = max(temp, dp[i+1][j+1] + 1)
		else:
			temp = max(temp, pre[j+1])
			# temp = max(temp, dp[i+1][j+1])
		temp = max(temp, pre[j])
		# temp = max(temp, dp[i+1][j])
		temp = max(temp, dp[j+1])
		# temp = max(temp, dp[i][j+1])
		dp[j] = temp
	# print(dp)
	dp, pre = [0 for i in range(n+1)], dp

print(pre[0])