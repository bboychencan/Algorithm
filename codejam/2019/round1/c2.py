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
		if len(word) == 0:
			root.isleaf = True
		else: 
			idx = ord(word[0]) - ord('A')
			if not root.nodes[idx]:
				root.nodes[idx] = TrieNode()
			self.insert_node(word[1:], root.nodes[idx])
			
class TrieNode:
	def __init__(self):
		self.isleaf = False
		self.nodes = [None for i in range(26)]
		# self.total = 0
		# self.suffix = ""


def dfs(trienode):
	unmat = 0
	if not trienode: return 0
	# print('trienode, suffix', trienode.total, trienode.suffix)
	if trienode.isleaf: 
		unmat += 1
	for i in range(26):
		u = dfs(trienode.nodes[i])
		unmat += u
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