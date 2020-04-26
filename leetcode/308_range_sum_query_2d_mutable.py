# 这道题基本上算是到目前为止写的行数最多的题了，题目本身难度并不是最高，只是2d的线段树写起来需要注意的corner case，各种边界条件
# 很多，写完后调试了很久。
# 这下基本把线段树算是摸熟了，定义一个线段树节点，定义一个buildtree，update，sum/max/min 函数。
# 然后其他的就比较直观了，只是注意一下细节即可。
# 这道题看了其他的答案更多地是采用BIT，而且代码明显更短，由此可见BIT跟线段树相比应该有他更有优势的地方，值得研究一下。

class SegTreeNode:
    def __init__(self, row1, col1, row2, col2):
        self.row1 = row1
        self.col1 = col1
        self.row2 = row2
        self.col2 = col2
        self.summ = 0
        self.lu = None
        self.ru = None
        self.lb = None
        self.rb = None
    
class NumMatrix:

    def build_tree(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        # print(r,c)
        return self.build_helper(0, 0, r-1, c-1, matrix)
        
    def build_helper(self, row1, col1, row2, col2, matrix):
        if row1 > row2 or col1 > col2: 
            # print('none tree', row1, col1, row2, col2)
            return None
        root = SegTreeNode(row1, col1, row2, col2)
        if row1 == row2 and col1 == col2:
            root.summ = matrix[row1][col1]
            return root
        midrow = (row1 + row2) // 2
        midcol = (col1 + col2) // 2
        root.lu = self.build_helper(row1,  col1, midrow, midcol, matrix)
        root.ru = self.build_helper(row1, midcol+1,midrow,  col2, matrix)
        root.lb = self.build_helper(midrow+1, col1,row2,  midcol, matrix)
        root.rb = self.build_helper(midrow+1,  midcol+1,row2, col2, matrix)
        root.summ += root.lu.summ if root.lu else 0
        root.summ += root.ru.summ if root.ru else 0
        root.summ += root.lb.summ if root.lb else 0
        root.summ += root.rb.summ if root.rb else 0
        return root
        
    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        self.root = self.build_tree(matrix)
    
    def update_helper(self, root, row, col, val):
        if root.row1 == root.row2 == row and \
            root.col1 == root.col2 == col:
            root.summ = val
            return
        midrow = (root.row1 + root.row2) // 2
        midcol = (root.col1 + root.col2) // 2
        child = None
        if row <= midrow and col <= midcol:
            child = root.lu
        elif row <= midrow and col > midcol:
            child = root.ru
        elif row > midrow and col <= midcol:
            child = root.lb
        elif row > midrow and col > midcol:
            child = root.rb 
        root.summ -= child.summ
        self.update_helper(child, row, col, val)
        root.summ += child.summ
        
    def update(self, row: int, col: int, val: int) -> None:
        self.update_helper(self.root, row, col, val)
    
    def sum_helper(self, root, row1, col1, row2, col2):
        # print('out', root == None)
        # print('sum helper', row1, col1, row2, col2)
        if root.row1 == row1 and root.col1 == col1 and \
            root.row2 == row2 and root.col2 == col2:
            # print('in', root == None)
            return root.summ
        midrow = (root.row1 + root.row2) // 2
        midcol = (root.col1 + root.col2) // 2
        res = 0
        if row2 <= midrow:
            if col2 <= midcol:
                return self.sum_helper(root.lu, row1, col1, row2, col2)
            elif col1 > midcol:
                return self.sum_helper(root.ru, row1, col1, row2, col2)
            else:
                return self.sum_helper(root.lu, row1, col1, row2, midcol) + \
                    self.sum_helper(root.ru, row1, midcol + 1, row2, col2)
        elif row1 > midrow:
            if col2 <= midcol:
                return self.sum_helper(root.lb, row1, col1, row2, col2)
            elif col1 > midcol:
                return self.sum_helper(root.rb, row1, col1, row2, col2)
            else:
                return self.sum_helper(root.lb, row1, col1, row2, midcol) + \
                    self.sum_helper(root.rb, row1, midcol + 1, row2, col2)
        else:
            if col2 <= midcol:
                return self.sum_helper(root.lu, row1, col1, midrow, col2) + \
                    self.sum_helper(root.lb, midrow+1, col1, row2, col2)
            elif col1 > midcol:
                return self.sum_helper(root.ru, row1, col1, midrow, col2) + \
                    self.sum_helper(root.rb, midrow+1, col1, row2, col2)
            else:
                return self.sum_helper(root.lu, row1, col1, midrow, midcol) + \
                    self.sum_helper(root.rb, midrow+1, midcol+1, row2, col2) + \
                    self.sum_helper(root.ru, row1, midcol+1, midrow, col2) + \
                    self.sum_helper(root.lb, midrow+1, col1, row2, midcol)
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: 
        # print('query')
        return self.sum_helper(self.root, row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)