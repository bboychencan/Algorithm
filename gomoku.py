# 用井字棋来练习minmax和alpha beta剪枝

class Move:
	def __init__(self, row, col):
		self.row = row
		self.col = col


class Gomoku:

	def __init__(self, rowlen, colen):
		self.maxval = 100
		self.minval = -100
		self.rowlen = rowlen
		self.collen = colen
		self.goallen = 3
		self.board = [["_" for i in range(self.collen)] for i in range(self.rowlen)]


	def display(self):
		[print(" ".join(x)) for x in self.board]
		print("")

	def evaluate(self, board):
		for row in range(self.rowlen):			
			for j in range(self.collen - self.goallen + 1):
				temp = ''.join(board[row][j:j+self.goallen])
				if temp == 'x' * self.goallen :
					return self.maxval
				elif temp == 'o' * self.goallen :
					return self.minval

		for col in range(self.collen):
			for j in range(self.collen - self.goallen + 1):
				temp = ''.join([board[x][col] for x in range(j,self.goallen)])
				if temp == 'x' * self.goallen :
					return self.maxval
				elif temp == 'o' * self.goallen :
					return self.minval

		for i in range(self.rowlen):
			for j in range(self.collen):
				count = 0
				piece = board[i][j]
				if piece == '_': continue
				x1, x2 = i, j
				while 0 <= x1 < self.rowlen and 0 <= x2 < self.collen:
					if board[x1][x2] == piece:
						count += 1
						x1 += 1
						x2 += 1
					else: 
						break
				x1, x2 = i - 1, j - 1
				count = 0
				while 0 <= x1 < self.rowlen and 0 <= x2 < self.collen:
					if board[x1][x2] == piece:
						count += 1
						x1 -= 1
						x2 -= 1
					else: 
						break
				if count == self.goallen: 
					return self.maxval if piece == 'x' else self.minval

				count = 0
				piece = board[i][j]
				x1, x2 = i, j
				while 0 <= x1 < self.rowlen and 0 <= x2 < self.collen:
					if board[x1][x2] == piece:
						count += 1
						x1 += 1
						x2 -= 1
					else: 
						break
				x1, x2 = i - 1, j + 1
				while 0 <= x1 < self.rowlen and 0 <= x2 < self.collen:
					if board[x1][x2] == piece:
						count += 1
						x1 -= 1
						x2 += 1
					else: 
						break
				if count == self.goallen: 
					return self.maxval if piece == 'x' else self.minval

		return 0

	def minmax(self, board, depth, ismaximizer):
		score = self.evaluate(board)

		if score == self.maxval: return self.maxval
		elif score == self.minval: return self.minval

		if ismaximizer:
			bestval = -1000
			for i in range(self.rowlen):
				for j in range(self.collen):
					if board[i][j] == '_':
						board[i][j] = 'x'
						val = self.minmax(board, depth + 1, False)
						bestval = max(bestval, val)
						board[i][j] = '_'
			return bestval

		else:
			bestval = 1000
			for i in range(self.rowlen):
				for j in range(self.collen):
					if board[i][j] == '_':
						board[i][j] = 'o'
						val = self.minmax(board, depth + 1, True)
						bestval = min(bestval, val)
						board[i][j] = '_'
			return bestval
		return 0


	def find_best_move(self, board, depth, ismaximizer):
		score = self.evaluate(board)
		bestmove = None

		if ismaximizer:
			bestval = -1000
			for i in range(self.rowlen):
				for j in range(self.collen):
					if board[i][j] == '_':
						board[i][j] = 'x'
						val = self.minmax(board, depth + 1, False)
						# print('move is {},{}, val is {}'.format(i,j,val))
						if val > bestval:
							bestmove = Move(i,j)
							bestval = max(bestval, val)
						board[i][j] = '_'
			return bestmove

		else:
			bestval = 1000
			for i in range(self.rowlen):
				for j in range(self.collen):
					if board[i][j] == '_':
						board[i][j] = 'o'
						val = self.minmax(board, depth + 1, True)
						if val < bestval:
							bestmove = Move(i,j)
							bestval = min(bestval, val)
						board[i][j] = '_'
			print("bot best move is {} {}, bestval is {}".format(bestmove.row, bestmove.col, bestval))
			return bestmove

	def is_move_left(self, board):
		for i in range(self.rowlen):
			for j in range(self.collen):
				if board[i][j] == '_': return True
		return False

	def is_game_end(self):
		score = self.evaluate(self.board)
		if score == self.maxval or score == self.minval or not self.is_move_left(self.board):
			return True
		else:
			return False


	def auto_play(self):
		# start from 'x' player
		player = True
		depth = 0
		print("The init board is: ")
		self.display()
		
		while not self.is_game_end():
			print("Current player is: {}".format(1 if player else 2))
			move = self.find_best_move(self.board, depth, player)
			player_no = 1 if player else 2
			if not move: 
				print("No best move for player ".format(player_no))
				break
			
			print("Player {}'s move is : ({}, {})".format(player_no, move.row, move.col))
			if player:
				self.board[move.row][move.col] = 'x'
			else:
				self.board[move.row][move.col] = 'o'
			self.display()
			player = not player
			depth += 1

		score = self.evaluate(self.board)
		if score == self.maxval:
			print("Player 1 Win!")
		elif score == self.minval:
			print("Player 2 Win!")
		else:
			print("Draw!")


	def play(self):
		depth = 0
		botmove = game.find_best_move(game.board, depth, False)
		depth += 1
		game.board[botmove.row][botmove.col] = 'o'

		while not game.is_game_end():
			while True:
				game.display()
				suggestmove = game.find_best_move(game.board, depth, True)
				if not suggestmove:
					print('no suggested move')

				else:
					print("Suggested move is {} {}".format(suggestmove.row, suggestmove.col))
				x, y = list(map(int, input("Please input row and col:\n").split()))
				if game.board[x][y] != '_':
					print("Invalid postion")
				else:
					game.board[x][y] = 'x'
					depth += 1
					break
			botmove = game.find_best_move(game.board, depth, False)
			if not botmove:
				print("No best move for player ".format(player_no))
				break
			game.board[botmove.row][botmove.col] = 'o'
			game.display()

		score = game.evaluate(game.board)
		if score == self.maxval:
			print("You Win!")
		elif score == self.minval:
			print("You Lose")
		else:
			print("Draw")	

if __name__ == "__main__":
	game = Gomoku(4,4)
	game.play()
	# game.display()

	# game.board = [
	# 	'_______________',
	# 	'x______________',
	# 	'x______________',
	# 	'x______________',
	# 	'x______________',
	# 	'x______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# 	'_______________',
	# ]
	# game.board = [
	# 	['o','o','x'],
	# 	['_','o','x'],
	# 	['x','_','_']
	# ]
	# print(game.evaluate(game.board))
	# bestmove = game.find_best_move(game.board, 0, True)
	# print('next best move is {}, {}'.format(bestmove.row, bestmove.col))












