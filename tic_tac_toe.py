# 用井字棋来练习minmax和alpha beta剪枝

class Move:
	def __init__(self, row, col):
		self.row = row
		self.col = col


class tic_tac_toe:

	def __init__(self, rowlen, colen):
		self.rowlen = rowlen
		self.collen = colen
		self.board = [["_" for i in range(3)] for i in range(3)]


	def display(self):
		[print(" ".join(x)) for x in self.board]
		print("")


	def evaluate(self, board):
		for row in range(3):
			if board[row][0] == board[row][1] == board[row][2]:
				if board[row][0]== 'x': 
					return 10
				elif board[row][0] == 'o': 
					return -10

		for col in range(3):
			if board[0][col] == board[1][col] == board[2][col]:
				if board[0][col] == 'x': 
					return 10
				elif board[0][col] == 'o': 
					return -10

		if board[0][0] == board[1][1] == board[2][2]:
			if board[0][0] == 'x': 
				return 10
			elif board[0][0] == 'o': 
				return -10

		if board[0][2] == board[1][1] == board[2][0]:
			if board[0][2] == 'x': 
				return 10
			elif board[0][2] == 'o': 
				return -10

		return 0

	def minmax(self, board, depth, ismaximizer):
		score = self.evaluate(board)

		if score == 10: return 10
		elif score == -10: return -10

		if ismaximizer:
			bestval = -1000
			for i in range(3):
				for j in range(3):
					if board[i][j] == '_':
						board[i][j] = 'x'
						val = self.minmax(board, depth + 1, False)
						bestval = max(bestval, val)
						board[i][j] = '_'
			return bestval

		else:
			bestval = 1000
			for i in range(3):
				for j in range(3):
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
			for i in range(3):
				for j in range(3):
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
			for i in range(3):
				for j in range(3):
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
		for i in range(3):
			for j in range(3):
				if board[i][j] == '_': return True
		return False

	def is_game_end(self):
		score = self.evaluate(self.board)
		if score == 10 or score == -10 or not self.is_move_left(self.board):
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
		if score == 10:
			print("Player 1 Win!")
		elif score == -1:
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
		if score == 10:
			print("You Win!")
		elif score == -10:
			print("You Lose")
		else:
			print("Draw")	

if __name__ == "__main__":
	game = tic_tac_toe(3,3)
	game.play()
	# game.board = [
	# 	['o','o','x'],
	# 	['_','o','x'],
	# 	['x','_','_']
	# ]
	# game.display()
	# bestmove = game.find_best_move(game.board, 0, True)
	# print('next best move is {}, {}'.format(bestmove.row, bestmove.col))












