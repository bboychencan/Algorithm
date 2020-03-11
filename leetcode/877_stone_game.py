# 877. Stone Game
from typing import Type
from typing import List


class Solution:
	def minmax(self, stones):
		if len(stones) == 1:
			return 'l', stones[0]
		elif len(stones) == 0:
			return 'l', 0
		total = sum(stones)
		d1, v1 = self.minmax(stones[1:])
		d2, v2 = self.minmax(stones[:-1])
		v1 = total - v1
		v2 = total - v2
		if v1 > v2:
			return ('l', v1)
		else:
			return ('r', v2)

	def stoneGame(self, piles: List[int]):
		res = self.minmax(piles)
		return res > sum(piles) - res

if __name__ == "__main__":
	s = Solution()
	bot = []
	human = []
	res = [5,3,4,5,12,34,33,12,8]
	print('array is :', res)
	d, val = s.minmax(res)
	if d == 'l':
		bot.append(res[0])
		print('bot selects l, {}, optimal val {}, human optimal val {}'.format(res[0], val, sum(res) - val))
		res = res[1:]
		print(res)
	elif d == 'r':
		bot.append(res[-1])
		print('bot selects r, {}, optimal val {},  human optimal val {}'.format(res[-1], val, sum(res) - val))
		res = res[:-1]
		print(res)

	while res:
		print("intput choice")  
		x = input()
		if x == 'l':
			human.append(res[0])
			res = res[1:]
			
		elif x == 'r':
			human.append(res[-1])
			res = res[:-1]
			
		else:
			print('invalid')
			break
		d, val = s.minmax(res)
		if d == 'l':
			bot.append(res[0])
			print('bot selects l, {}, optimal val {}, human optimal val {}'.format(res[0], val, sum(res) - val))
			res = res[1:]
			print(res)
		elif d == 'r':
			bot.append(res[-1])
			print('bot selects r, {}, optimal val {},  human optimal val {}'.format(res[-1], val, sum(res) - val))–
			res = res[:-1]
			print(res)
		print('human :', human, 'score :', sum(human))
		print('bot :', bot, 'score :', sum(bot))
