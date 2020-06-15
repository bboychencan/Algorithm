# I got really frustrated with this solution.
# It works perfectly with the provided test cases, and in my mind.
# But still failed in the submission, I can't figure out which part is wrong.
# It took me hours. Then I decided to write a program to create random generate test cases.
# Since I already have a AC solution b2.py, I just compare the ouput of them and try to find test cases 
# that got different result.
# Finally, after hours of struggling, I finally found out a test case I want.
# B, A, BBAAB, BBA, BBBABB, AAABB

# This reminds me of a post I read before, it says there are two types of engineer.
# Type 1 will make sure the algorithm is clear and corrent and then start to implement and provide test 
# cases by themselves. Type2 will rely on the provided test cases, and program against the test cases.
# modify a little whenever it got error. 
# The efficiency of type 1 is 10X more than type 2. 
# Then, I think maybe I used to the type 2 programmer.
# I'm not comfortable with problems without enough test cases, and I'm not good at coming up with test
# cases on my own, I rely on the test cases too much, especially on leetcode, which provides all the unpassed
# test cases... That's why I feel painful when programming on codeforces or nowcoder... cause they 
# don't give feedback...
# OH MY GOD! I finally learn this today. As a good programmer, I shouldn't rely on the error as feedback.
# I should think through the algorithm carefully and make sure it work correctly, and provide various test cases
# on my own, which proves I fully understand the problem and the algorithm, and aware of which part maybe tricky...

# This is really a good lesson.
import math
from collections import defaultdict
import heapq
from itertools import permutations
from itertools import combinations
from collections import Counter

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		self.insert_node(word, self.root)

	def insert_node(self, word, root):
		if len(word) > 0:
			idx = ord(word[0]) - ord('A')
			if not root.nodes[idx]:
				root.nodes[idx] = TrieNode()
			self.insert_node(word[1:], root.nodes[idx])
		root.total += 1
			
class TrieNode:
	def __init__(self):
		self.nodes = [None for i in range(26)]
		self.total = 0
		# self.suffix = ""


def dfs(trienode):
	unmat = 0
	if not trienode or trienode.total == 0: return 0
	if trienode.total == 2:
		return 0
	elif trienode.total == 1:
		return 1
	else:
	# print('trienode, suffix', trienode.total, trienode.suffix)
	# if trienode.isleaf: 
		total = 0
		for i in range(26):
			u = dfs(trienode.nodes[i])
			if trienode.nodes[i]:
				total += trienode.nodes[i].total
			unmat += u
		# After struggling for hours, I finally figured out I did not check
		# the case that the trienode by it self is a leafnode, in which case
		# the sum of the return results of its children nodes will not be equal
		# to the toal stored in this trienode!
		unmat += trienode.total - total
		if unmat >= 2:
			unmat -= 2
		return unmat

def test_case():
	N = int(input())
	words = [] 
	for i in range(N):
		words.append(input())
	trie = Trie()
	for word in words:
		trie.insert(word[::-1])
	unmat = 0
	# print('trie total', trie.root.total)
	for i in range(26):
		u = dfs(trie.root.nodes[i])
		unmat += u
	print(len(words) - unmat)	



def main():
    T = int(input())
    for i in range(1, T+1):
        print("Case #{}: ".format(i), end = "")
        test_case()


if __name__=="__main__":
	main()