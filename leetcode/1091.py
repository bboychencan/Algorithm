# Leetcode 1091 shortest path in binary matrix

from collections import deque
import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0 for i in range(n)] for i in range(n)]
        scores = {(0,0): 2*n - 2}
        directs = [[0,1],[0,-1],[-1,0],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        distance = [[10000 for i in range(n)] for i in range(n)]
        layers = 0
        queue = []
        if grid[0][0] == 0:
            distance[0][0] = 1
            queue.append((2*n-2,1,0,0))
            visited[0][0] = 1
        
        while queue:            
            prio, dist, px,py = heapq.heappop(queue)
            # dist = distance[px][py]
            if px == n-1 and py == n-1: return dist
            for dx, dy in directs:
                if 0 <= px + dx < n and \
                0 <= py + dy < n and \
                grid[px+dx][py+dy] == 0 and \
                visited[px+dx][py+dy] == 0:
                    g = dist + 1
                    h = max(n-1-px-dx, n-1-py-dy)
                    f = g + h
                    if f < scores.get((px+dx,py+dy), float('inf')):
                        scores[(px+dx,py+dy)] = f
                        heapq.heappush(queue, (f, g, px+dx, py+dy))

        return -1

# 这一题第一眼看完就立刻写了一个BFS的解答，AC了。 不过看了下讨论有人提到用Astar，正好Astar用的不是很熟所以打算学习一下自己写一遍。
# 看了一些答案和blog，感觉讲的很清楚，Astar并不难，主要是f=g+h，g是出发点到当前点的距离，h是启发式对当前节点到终点距离的估算，有manhattan，euclidean, Chebyshev几种。
# 有个答案写的很好，把Astar算法分了个小模块，很容易记忆，不过有点冗长，像是产品代码，不适合做竞赛。大概思路如下
# 定义几个method，get_heuristic（）用来估算距离，get_successor()用来搜索当前节点的子节点，priority_queue，在 python里利用heapq的特点，将priority值存在tuple的第一位，get_goal()用来
# 判断是否到达终点。reconstruct_path()用来重建最优路径，这个因为本题没有要求，所以就没有写，但这点很重要，基本的思想是存储每个节点的父亲节点，这样当找到最优的节点时，一次寻找父节点即可。
# 我自己写的答案，没有整理成这么几个模块。不过在自己写的时候遇到了很严重的一个问题，我之前没有考虑到过的。 
## 为了解释这个问题，首先说一下我如何写bfs的，在bfs中，在visit不同的节点的时候有可能得到重复的后继节点，这样如果不去处理这种重复，必然会TLE，我的处理方法是在把后继节点添加到queue中的时候，
## 进行判断，是否visited过，这里的visit的定义是作为后继节点被遍历到，而非从queue中pop出来，这一点就保重每个点只会出现在queue中一次。避免了重复。
## 而在写Astar的时候，我的存储用的heapq，但是仍然用了bfs的思路，结果犯了错误。我依然是把每个遍历到的后继节点标记为visit，用这种方式来避免重复计算，但是问题就出在这里，由于Astar不能像bfs一样保证
## 只要遍历到的后继节点一定是最优的路径到达的，在Astar中，heapq的排序是依据g+h而非单据依据g，这样的话有可能首次遍历到的后继节点有可能有其他更快的路径遍历到，但是由于已经被标记成visit了，所以就
## 没有被更新，正是由于这个，我的程序WA了。仔细检查了一下，发现别人采用的方法是，在遍历到后继节点时做一个判断，不是简单的visit的判断，而是判断之前的f值或者g值（f或者g都试验了，都可以）是否比当前的要大
## 如果是的话，那么用当前更小的值去更新，这样的话避免大量重复遍历后继节点，同时也保证了最优值永远都会在heapq中，学到了。 以上。
## 同时，为了打印路径，需要记录parent节点，这个节点也在上面f值或g值判断的时候，进行更新。这样就保证当前节点可以有最近到达路线。

# 另外一个还没完全搞明白的是，如何证明用启发式函数做heapq一定不会漏掉最优解，这个应该会牵扯到具体的数学证明，留作以后有时间再研究。
# 第一次独立完整地写完Astar算法很开心，记录一下。