class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[float('inf') for i in range(k+1)] for i in range(n)] for i in range(m)]
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        vis = [[0 for i in range(n)] for i in range(m)]
        
        def dfs(x, y, c):
            if dp[x][y][c] != float('inf'):
                return dp[x][y][c]
            if x == m-1 and y == n-1:
                return 0
            
            res = float('inf')
            for i, j in dirs:
                if 0 <= x+i < m and 0 <= y+j < n and vis[x+i][y+j] == 0:
                    if grid[x+i][y+j] == 1:
                        if c >= 1:
                            vis[x+i][y+j] = 1
                            res = min(res, dfs(x+i, y+j, c-1) + 1)
                            vis[x+i][y+j] = 0
                        else:
                            continue
                    elif grid[x+i][y+j] == 0:
                        vis[x+i][y+j] = 1
                        res = min(res, dfs(x+i, y+j, c) + 1)
                        vis[x+i][y+j] = 0
                        
            dp[x][y][c] = res
            return res
        
        res = dfs(0, 0, k)
        if res == float('inf'): return -1
        else: return res
