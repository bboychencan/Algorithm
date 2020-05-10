import heapq

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        q = []
        q.append((m-1+n-1, 0, 0, 0, k))
        
        vis = set()
        
        while q:
            f, g, x, y, c = heapq.heappop(q)
            if x == m-1 and y == n-1:
                return g
            
            for dx, dy in dirs:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    if grid[x+dx][y+dy] == 1 and c > 0:
                        if (x+dx, y+dy, c-1) not in vis:
                            h = (m-1 - x-dx + n-1 -y - dy)
                            vis.add((x+dx, y+dy, c-1))

                            heapq.heappush((g+1+h, g+1, x+dx, y+dy, c-1))
                    elif grid[x+dx][y+dy] == 0:
                        if (x+dx, y+dy, c) not in vis:
                            h = (m-1 - x - dx + n-1-y-dy)
                            vis.add((x+dx, y+dy, c))
                            heapq.heappush((g+1+h, g+1, x+dx, y+dy, c))
        return -1