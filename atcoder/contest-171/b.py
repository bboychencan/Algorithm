n, k = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices = sorted(prices)
print(sum(prices[:k]))	