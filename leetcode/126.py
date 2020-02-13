class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        pre = collections.defaultdict(list)
        if endWord not in words: return []
        elif beginWord in words: words.remove(beginWord)
        
        queue = collections.deque([])
        queue.append(beginWord)
        level = 1
        
        
        def createseq(word):
            res = []
            if not pre[word]:
                res.append([word])
            for w in pre[word]:
                temp = createseq(w)
                for x in temp:
                    x.append(word)
                res.extend(temp)
            return res

        while queue:
            n = len(queue)
            visits = set()
            for i in range(n):
                top = queue.popleft()
                if top == endWord: 
                    return createseq(top)
                for j in range(len(top)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        temp = top[:j] + c + top[j+1:]
                        if temp != top and temp in words:
                            pre[temp].append(top)
                            if temp not in visits:
                                visits.add(temp)
                                queue.append(temp)
            words -= visits
        return []
            
        
        
# 这道题wordladder II 由于做过wordladder I，所以对于基本部分很熟悉，就是BFS。其中一个技巧为了降低每两个word比较带来的复杂度，利用了逐个修改每一位的字符25次遍历所有的相邻word降低了复杂度。
# 另外一点，这一题需要返回全部数列，第一反应是，需要记录每个node的前继node，这里面牵涉到如果一个节点同时被多个节点访问应该如何处理的情况，稍加思考发现只要保证每个新被访问的节点都是在同一个level内出现的
# 那么只需要把该level里的所有前继节点记录下来即可。 
# 最后关于打印全部数列，想到了用递归的方法，这样的话代码比较简单，不需要手动写loop遍历各种边界情况。
# 很快就AC了，还是比较有成就感:)

# 发现答案里有一个巧妙的python comprehension不用递归的方法返回全部数列，感觉很巧妙
#     while res and res[0][0] != start:
#        res = [[p]+r for r in res for p in parents[r[0]]]
