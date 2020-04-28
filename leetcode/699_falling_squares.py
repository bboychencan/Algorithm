# When dealling sparse points on large coordinates, we can use coordinates compression.
# combined with segment tree. This is very powerful

class SegTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.leftnode = None
        self.rightnode = None
        self.m = 0

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        def buildtree(l, r):
            root = buildhelper(l, r)
            return root
        
        def buildhelper(l, r):
            if l == r:
                root = SegTreeNode(l, r)
                root.m = 0
                return root
            root = SegTreeNode(l, r)
            mid = (l + r) // 2
            root.leftnode = buildhelper(l, mid)
            root.rightnode = buildhelper(mid + 1, r)
            root.m = 0
            return root
        
        def find(l, r):
            return findhelper(root, l, r)
            
        def findhelper(root, l, r):
            if l == root.l and root.r == r: 
                return root.m
            
            mid = (root.l + root.r) // 2
            if r <= mid:
                return findhelper(root.leftnode, l, r)
            elif l > mid:
                return findhelper(root.rightnode, l, r)
            else:
                
                a = findhelper(root.leftnode, l, mid)
                b = findhelper(root.rightnode, mid+1, r)
                # print('here', a, b)
                return max(a, b)
        
        def update(l, r, val):
            updatehelper(root, l, r, val)
        
        def updatehelper(root, l, r, val):
            if root.l <= l <= root.r or root.l <= r <= root.r:
                root.m = max(root.m, val)
            if root.l == root.r: return
            
            mid = (root.l + root.r) // 2
            if r <= mid:
                updatehelper(root.leftnode, l, r, val)
            elif l > mid:
                updatehelper(root.rightnode, l, r, val)
            else:
                updatehelper(root.leftnode, l, mid, val)
                updatehelper(root.rightnode, mid+1, r, val)
        
        points = set()
        for l, s in positions:
            points.add(l)
            points.add(l+s-1)
        
        points = sorted(points)        
        n = len(points)
        root = buildtree(0, n)
        res = []
        mapp = {v: i for i,v in enumerate(points)}
        
        for l, s in positions:
            m = find(mapp[l], mapp[l + s - 1])
            
            update(mapp[l], mapp[l+s-1], m + s)
            afterm = find(mapp[l], mapp[l + s - 1])
            # print('main', l,s,m, afterm, find(0, 1000))
            res.append(find(0, n))
        
        return res
            