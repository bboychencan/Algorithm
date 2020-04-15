import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

def get_elim_score(elims, board):
	res = 0
	for x, y in elims:
		res += board[x][y]
	return res

def find_elims(dancers, board, neighbors):
	elims = set()

	for d in dancers:
		count = 0
		total = 0
		for i in range(4):
			neig = neighbors[d][i]
			# print('dancer neigbor, equals 0?', d, neig, neig == 0)
			if neig != 0:
				count += 1
				total += board[neig[0]][neig[1]]

		if count > 0 and board[d[0]][d[1]] < total / count:
			# print('dancer, total, count', d, total, count, total / count)
			elims.add(d)

	# print('elims', elims, neighbors)

	return elims

def update_neighber_dancer(dancer, elims, newelims, neighbors, board):
	if dancer in elims:
		pass
	else:
		count = 0
		total = 0
		iselim = False
		for i in range(4):
			neig = neighbors[dancer][i]
			if neig != 0:
				count += 1
				total += board[neig[0]][neig[1]]
		if count > 0:
			iselim = board[dancer[0]][dancer[1]] < total / count

		if iselim:
			newelims.add(dancer)
		elif dancer in newelims:
			newelims.remove(dancer)


def remove_update(elims, neighbors, board):
	newelims = set()
	for d in elims:
		neig = neighbors[d]
		# print('d, n', d, neig)
		if neig[0] != 0:
			neighbors[neig[0]][2] = neig[2]
			update_neighber_dancer(neig[0], elims, newelims, neighbors, board)
		if neig[1] != 0:
			neighbors[neig[1]][3] = neig[3]
			update_neighber_dancer(neig[1], elims, newelims, neighbors, board)
		if neig[2] != 0:
			neighbors[neig[2]][0] = neig[0]
			update_neighber_dancer(neig[2], elims, newelims, neighbors, board)
		if neig[3] != 0:
			neighbors[neig[3]][1] = neig[1]
			update_neighber_dancer(neig[3], elims, newelims, neighbors, board)

	# print(elims, dancers)
	# dancers -= elims
	# print(elims, dancers)
	# print(dancers)
	return newelims

def test_case():
	r, c = list(map(int, input().split()))
	# print('r,c',r,c)
	board = [[] for i in range(r)]
	nb = {}
	total = 0

	for i in range(r):
		# print('start')
		temp = input().split()
		# print(temp, list(map(int, temp)))
		board[i] = list(map(int, temp))
		total += sum(board[i])

	for i in range(r):
		for j in range(c):
			temp = [0 for  i in range(4)]
			if i - 1 >= 0:
				temp[0] = (i-1, j)
			if j - 1 >= 0:
				temp[1] = (i ,j-1)
			if i + 1 < r:
				temp[2] = (i+1, j)
			if j + 1 < c:
				temp[3] = (i, j+1)
			nb[(i, j)] = temp

	dancers = set(nb.keys())
	pre = total
	elims = find_elims(dancers, board, nb)

	while len(elims) > 0:
		# print('elims', elims)
		score = get_elim_score(elims, board)
		elims = remove_update(elims, nb, board)
		pre -= score
		total += pre
		# elims = find_elims(dancers, board, nb)

	print(total)



def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()