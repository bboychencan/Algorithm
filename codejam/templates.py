## BIT
def __init__(self, nums: List[int]):
	self.nums = [0] + nums[::]
	n = len(self.nums)
	self.BIT = [0] * (n)
	# BIT starts from 1
	for i in range(1, n):
		for j in range(i - self.lowbit(i) + 1, i+1):
			self.BIT[i] += self.nums[j]
   
def lowbit(self, x):
	return x & -x

def update(self, i: int, val: int) -> None:
	idx = i+1
	diff = val - self.nums[idx]
	self.nums[idx] = val
	while idx < len(self.nums):
		self.BIT[idx] += diff
		idx += self.lowbit(idx)

def presum(self, i):
	res = 0
	while i >= 1:
		res += self.BIT[i]
		i -= self.lowbit(i)
	return res

def sumRange(self, i: int, j: int) -> int:
	res = self.presum(j+1) - self.presum(i)
	return res


## Segment Tree
class SegTreeNode:
    def __init__(self, start, end, summ):
        self.start = start
        self.end = end
        self.sum = summ
        self.left = None
        self.right = None
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums)
    
    def buildhelper(self, start, end, nums):
        if start == end:
            root = SegTreeNode(start, end, nums[start])
            return root
        mid = (start + end) // 2
        root = SegTreeNode(start, end, sum(nums[start:end+1]))
        root.left = self.buildhelper(start, mid, nums)
        root.right = self.buildhelper(mid+1, end, nums)
        return root
    
    def build(self, nums):
        if len(nums) <= 0: return None
        return self.buildhelper(0, len(nums) - 1, nums)
        
    def update(self, i: int, val: int) -> None:
        self.updatehelper(self.root, i, val)
        
    def updatehelper(self, root, i, val):
        if root.start == root.end and root.end == i:
            root.sum = val
            return
        mid = (root.start + root.end) // 2
        if i <= mid:
            self.updatehelper(root.left, i, val)
            root.sum = root.left.sum + root.right.sum
        else:
            self.updatehelper(root.right, i, val)
            root.sum = root.left.sum + root.right.sum
        
    def sumrangehelper(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        mid = (root.start + root.end) // 2
        if j <= mid:
            return self.sumrangehelper(root.left, i, j)
        elif i > mid:
            return self.sumrangehelper(root.right, i, j)
        else:
            return self.sumrangehelper(root.left, i, mid) + \
                self.sumrangehelper(root.right, mid+1, j)
        
    def sumRange(self, i: int, j: int) -> int:
        return self.sumrangehelper(self.root, i, j)     



# A star
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

# Extcrt
# 
# Bezout Lemma
# ax + by = gcd(a, b)

# To get x, y
# We use the same strategy of Euclidean way to get gcd(a, b)
# The only difference is that in addition to the original procedure, we keep track 
# of s, t
# s0 = 1, s1 = 0, t0 = 0, t1 = 1
# si+1 = si-1 - qisi, ti+1 = ti-1 - qiti

def ext_euclid(a, b):
	r1, r2 = a, b
	s1, s2 = 1, 0
	t1, t2 = 0, 1
	while r2 != 0:
		q = r1 // r2
		r1, r2 = r2, r1 - q * r2
		s1, s2 = s2, s1 - q * s2
		t1, t2 = t2, t1 - q * t2
	return s1, t1, r1

def gcd(a, b):
	while b != 0:
		t = a % b
		a = b
		b = t
	return a

def main():
    a, b = list(map(int, input().split()))
    print(gcd(a, b))
    print(ext_euclid(a, b))

# Fast power
def fast_power(a, n):
	if n == 0: return 1
	res = 1
	while n > 0:
		if n & 1 == 1:
			res *= a
		a = a * a
		n = n >> 1
	return res

def brute_force(a, n):
	res = 1
	for i in range(n):
		res *= a
	return res

# Tarjan
def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        low = [float('inf')] * n
        dfn = [float('inf')] * n
        parent = [-1] * n
        graph = [[] for i in range(n)]
        visit = [0] * n
        stack = []
        self.count = 0
        self.res = []
        
        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(x):
            stack.append(x)
            visit[x] = 1
            dfn[x] = self.count
            self.count += 1
            low[x] = dfn[x]
            
            for a in graph[x]:
                if not visit[a]:
                    parent[a] = x
                    dfs(a)
                elif parent[x] != a:
                    low[x] = min(low[a], low[x])
            
            top = stack.pop()
            if stack:
                if dfn[stack[-1]] < low[top]:
                    self.res.append([top, stack[-1]])
                else:
                    low[stack[-1]] = min(low[stack[-1]], low[top])
        
        dfs(0)
        return self.res


# Union Find
def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [-1] * len(edges)
        rank = [1] * len(edges)
        visited = [0] * len(edges)
        error1 = []
        error2 = []
        
        def find(k: int):
            if parents[k] == -1:
                return k
            parents[k] = find(parents[k])
            return parents[k]
        
        def union(a: int, b: int) -> bool:
            roota = find(a)
            rootb = find(b)
            if roota == rootb:
                return False
            if rank[roota] > rank[rootb]:
                parents[rootb] = roota
            elif rank[roota] < rank[rootb]:
                parents[roota] = rootb
            else:
                parents[roota] = rootb
                rank[rootb] += 1
            return True
        
        for x, y in edges:
            if visited[y - 1] == 1:
                error2 = [x - 1, y - 1]
            visited[y - 1] = 1
        if error2 == []:
            for x, y in edges:
                if not union(x - 1, y - 1):
                    return [x, y]
        else:
            iscircle = False
            for x, y in edges:
                if [x - 1, y -1] == error2:
                    continue
                elif y - 1 == error2[1]:
                    error1 = [x -1, y - 1]
                if not union(x - 1, y - 1):
                    iscircle = True
                    break

            if iscircle:
                return [error1[0] + 1, error1[1] + 1]
            else:
                return [error2[0] + 1, error2[1] + 1]



# Minmax

def miniMaxScore(i, j, wantMax=True):
	if i > j: return 0
	if wantMax:
	    if maxScore[i][j] != MININT: return maxScore[i][j]
	    maxScore[i][j] = max(
	        piles[i] + miniMaxScore(i + 1, j, False),
	        piles[j] + miniMaxScore(i, j - 1, False),
	    )
	    return maxScore[i][j]
	else:
	    if minScore[i][j] != MAXINT: return minScore[i][j]
	    minScore[i][j] = min(
	        -piles[i] + miniMaxScore(i + 1, j, True),
	        -piles[j] + miniMaxScore(i, j - 1, True),
	    )
	    return minScore[i][j]