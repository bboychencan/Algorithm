import math

def test_case():
	n = int(input())
	visited = set()
	next_node = {}
	res = []
	visited.add((1,1))
	if dfs(1, 1, 1, visited, next_node, n):
		print(1, 1)
		r, k = (1, 1)
		while (r,k) in next_node:
			r, k = next_node[(r, k)]
			print(r, k)
			
def poss_moves(r, k, n):
	# print('start find moves', r, k, n)
	res = []
	if r - 1 >= 1 and k - 1 >= 1:
		res.append((r-1, k-1))
	if r - 1 and k <= r - 1:
		res.append((r-1, k))
	if k - 1 >= 1:
		res.append((r, k-1))
	if k + 1 <= r:
		res.append((r, k+1))
	if r + 1 <= 500:
		res.append((r+1, k))
	if r + 1 <= 500 and k + 1 <= r + 1:
		res.append((r+1, k+1))

	# print('checking moves', res)	
	res = sorted(res, key=lambda x: n - (get_ele(x[0], x[1])))

	return res

def get_ele(r, k):
	# print('here', r, k)
	return math.factorial(r - 1) // math.factorial(k - 1) // math.factorial(r-k)

def dfs(r, k, s, visited, next_node, n):
	# print('here', s, n)
	if s == n:
		return True
	elif s > n:
		return False
	else:
		for rn, kn in poss_moves(r, k, n):
			if (rn, kn) in visited: continue

			visited.add((rn, kn))
			next_node[(r, k)] = (rn, kn)
			snew = s + get_ele(rn, kn)
			# print(rn,kn,snew)
			if dfs(rn, kn, snew, visited, next_node, n):
				return True
			visited.remove((rn, kn))
			del next_node[(r, k)]
	return False

def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i))
        test_case()

main()