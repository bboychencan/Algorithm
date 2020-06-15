import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter


def get_score(board):
	res = 0
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] != -1:
				res += board[i][j]

	return res

def get_elim_score(elims, board):
	res = 0
	for x, y in elims:
		if board[x][y] != -1:
			res += board[x][y]
	return res

def find_elims(board):
	elims = []
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == -1: continue
			neib = []
			for k in range(i+1, len(board)):
				if board[k][j] != -1:
					neib.append((k,j))
					break
			for k in range(i-1, -1,-1):
				if board[k][j] != -1:
					neib.append((k,j))
					break
			for k in range(j+1, len(board[0])):
				if board[i][k] != -1:
					neib.append((i,k))
					break
			for k in range(j-1, -1, -1):
				if board[i][k] != -1:
					neib.append((i,k))
					break

			total = 0
			for x, y in neib:
				total += board[x][y]
			# print('i,j,neib', i, j, neib)
			if len(neib) > 0 and board[i][j] < total / len(neib):
				elims.append((i,j))

	# print('here', board, elims)
	return elims

def remove(elims, board):
	for x, y in elims:
		board[x][y] = -1


def test_case():
	r, c = list(map(int, input().split()))
	# print('r,c',r,c)
	board = [[] for i in range(r)]
	for i in range(r):
		# print('start')
		temp = input().split()
		# print(temp, list(map(int, temp)))
		board[i] = list(map(int, temp))

	# print('cal')
	round = 0
	total = get_score(board)
	pre = total
	elims = find_elims(board)

	while len(elims) > 0:
		# print('elims', elims)
		score = get_elim_score(elims, board)
		remove(elims, board)
		pre -= score
		total += pre
		elims = find_elims(board)

	print(total)



def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()