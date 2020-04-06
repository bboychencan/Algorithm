# 很多年前觉得这个题目还有点难度
# 今天2020/04/03再写一下检验一下自己的水平
# 基本思路就是用dfs返回所有的可能解

class Solution:
	def __init__(self):
		self.n = 8
		self.board = [0] * self.n
		self.res = []

	def eightQueens(self):
		board = self.board.copy()
		self.dfs(board, 0)
		return self.res

	def display(self):
		for i in range(len(self.res)):
			print("Solution {}".format(i+1))
			for j in self.res[i]:
				temp = [0] * self.n
				temp[j] = 1
				print("".join(list(map(str, temp))))
				# [print(x) for x in temp]

	def dfs(self, board, row):
		if row == self.n:
			self.res.append(board.copy())
			return

		for i in range(self.n):
			board[row] = i 
			if self.check(board, row):
				self.dfs(board, row + 1)
			board[row] = 0
		return 

	def check(self, board, row) -> bool:
		x = board[row]
		for i in range(row):
			if board[i] == board[row] or abs(board[i] - board[row]) == abs(row - i):
				return False
		else:
			return True


def main():
	s = Solution()
	res = s.eightQueens()
	s.display()


if __name__=="__main__":
	main()



## 写完之后感觉挺简单，然后尝试着分析了下时间复杂度，发现这似乎跟直接做暴力求解没啥区别？ 都可以是N！，只是在暴力的时候做验证比较复杂一些，需要两两比对所有皇后，O(N! * N^2)
## 哦不对，这里的暴力法并非暴力法，python里面可以生成所有全排列，这个复杂度是O(N!)，但是如果暴力解的话生成所有全排列需要O(N^N)?
## 而回溯法在进行验证的时候只需要O(N) 时间复杂度就是 O(N! * N)