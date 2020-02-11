# import heapq
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:return 0
        n = len(wordList)                
        # def getdist(x, y):
        #     count = 0
        #     for i in range(len(x)):
        #         if x[i] != y[i]:
        #             count += 1
        #     return count
                
        visited = [0] * n
        queue = deque([])
        queue.append(beginWord)
        
        level = 1
        while queue:
            size = len(queue)
            for i in range(size): 
                word = queue.popleft()
                if word == endWord: 
                    return level
                else:
                    for j in range(len(word)):
                        temp = list(word)
                        for k in range(26):
                            if chr(ord('a') + k) != temp[j]:
                                temp[j] = chr(ord('a') + k)
                                newword = "".join(temp)
                                if newword in wordList:                              
                                    queue.append(newword)
                                    wordList.remove(newword)
            level += 1
        return 0

# 这一道题，第一反应就知道是一个bfs，然后写完之后超时了，琢磨了半天在怀疑是不是自己的bfs写的效率不高，尝试用heapq去做一些启发搜索，但是一直超时，而且启发的时候如果不把level放在第一有些级会出现错误结果。
# 看了答案后，发现这个题的关键在于计算这个**只更改一个字符**的距离。 我使用的方法是针对每两个word比较他们的距离，这样的复杂度就等于wordlen * n * n。
# 而有一个巧妙的方法，针对每一个word，把所有跟他距离唯一的word都求出来，然后判断是否在现存dict中，这样由于hash操作复杂度为O(1)，那么这个方案的复杂度只有wordlen * 26 * n，在n很大的时候改善很明显。
# 所以这里面关键是，忘记了用hashset来存储这些word，他的查找时间O(1)非常优秀!