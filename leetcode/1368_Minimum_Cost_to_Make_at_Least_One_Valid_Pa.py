# 1368. Minimum Cost to Make at Least One Valid Path in a Grid
from collections import deque 
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1: return 0
        visited = set()
        dirs = [[0,0], [0,1],[0,-1],[1,0],[-1,0]]
        # dp = [[-1 for i in range(n)] for i in range(m)]
        # dp[m-1][n-1] = 0
        queue = deque([])
        
        def getPoints(x,y):
            points = []
            o = grid[x][y]
            dx = dirs[o][0]
            dy = dirs[o][1]
            while 0 <= x + dx < m and 0 <= y + dy < n and (x+dx, y+dy) not in visited:
                visited.add((x+dx, y+dy))
                points.append((x+dx, y+dy))
                x = x+dx
                y = y+dy
                o = grid[x][y]
                dx = dirs[o][0]
                dy = dirs[o][1]
#             print(points)
            return points
            
        queue.extend(getPoints(0,0))
        steps = 0
        if not queue:
            steps += 1
            arrow = grid[0][0]
            for i in range(1,5):
                if i != arrow:
                    grid[0][0] = i
                    points = getPoints(0,0)
                    queue.extend(points)
                    grid[0][0] = arrow

                    
        while queue:
#             print(queue)
            length = len(queue)
            for i in range(length):
                x,y = queue.popleft()
                if x == m-1 and y == n-1: return steps
                arrow = grid[x][y]
                for i in range(1, 5):
                    if i != arrow:
                        grid[x][y] = i
                        points = getPoints(x,y)
#                         print(points)
#                         print(queue)
                        queue.extend(points)
                        grid[x][y] = arrow
            steps += 1
        return steps

                    
# 这一道题猛一看有点慌，感觉之前没有见过类似的题目，稍微冷静了一下，想了一个dfs的解法，输入测试样例都正确，开始觉得
# 有点小开心，可谁知提交后TLE。
# 然后就开始有点慌了，又开始想是不是可以用dp存储中间结果，但是直觉觉得不能用dp，因为这个dp在计算的时候默认要改变一些节点，
# 而在计算其他的节点的dp的时候可能并没有改变某一节点。
# 还是写完了dp，结果不出所料WA了。
# 这下心态要崩了，又抓紧搜刮脑海里的idea，回想到了我刚写了Astar算法，这个题应该不算什么。通然想到，这个似乎可以用bfs的方法，
# 稍微一考虑，立刻就得到了办法，可是写完了也超时了几分钟，最终答案正确还是很欣慰。

# 看了高手的讨论，发现还是有些可以改进的地方，毕竟我的写法还是有些臃肿。
# 他的思路很清晰，dfs + bfs， 两部很简明。
def minCost(self, A):
        n, m, inf, k = len(A), len(A[0]), 10**9, 0
        dp = [[inf] * m for i in xrange(n)]
        dirt = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        bfs = []

        def dfs(x, y):
            if not (0 <= x < n and 0 <= y < m and dp[x][y] == inf): return
            dp[x][y] = k
            bfs.append([x, y])
            dfs(x + dirt[A[x][y] - 1][0], y + dirt[A[x][y] - 1][1])

        dfs(0, 0)
        while bfs:
            k += 1
            bfs, bfs2 = [], bfs
            [dfs(x + i, y + j) for x, y in bfs2 for i, j in dirt]
        return dp[-1][-1]

