# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # two ways
        # 1, use pre
        pre = TreeNode(-float('inf'))
        
        def valid(node):
            if node == None: return True
            if not valid(node.left): return False
            nonlocal pre
            if node.val <= pre.val : return False
            pre = node
            if valid(node.right):
                return True

        return valid(root)
        # 2, use pure min, max interval

# 这道题很久前做过，写的比较复杂，把1年的解贴下来做个参考
# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode(int x) { val = x; }
#  * }
#  */
# class Solution {
#     public boolean isValidBST(TreeNode root) {
#         if(root == null) return true;
#         boolean judgeLeft = false;
#         boolean judgeRight = false;
#         if(root.left == null 
#            || (root.left != null && getRightMost(root.left) < root.val && isValidBST(root.left)))
#             judgeLeft = true;
         
#         if(root.right == null || 
#            (root.right != null && getLeftMost(root.right) > root.val && isValidBST(root.right))) judgeRight = true;
        
#         if(judgeLeft && judgeRight) return true;
#         else return false;
#     }
    
#     private int getRightMost(TreeNode root){
#         TreeNode temp = root;
#         int max = root.val;
#         while(temp != null){
#             max = temp.val;
#             temp = temp.right;
#         }
#         return max;
#     }
    
#     private int getLeftMost(TreeNode root){
#         TreeNode temp = root;
#         int min = root.val;
#         while(temp != null){
#             min = temp.val;
#             temp = temp.left;
#         }
#         return min;
#     }
# }

# 可以看出以前的思路，虽然知道用recursive，但是还需要专门的method去算左边最大值，
# 及右边最小值，相当的臃肿，而且重复。
# 对于BST类的题目我总觉得很容易理解，无非就是递归，中序，前序，后序排列这样。但是
# 由于没有做过针对的专项训练，导致遇到这类问题的变种，不能很快想出最优的，最漂亮
# 最简化的答案出来，尤其是在涉及到求前K和，最大值等的问题，没有明确的思路应该在递归
# 的循环里计算和存储什么值，导致花费时间较多，且效率不高。
# 总结来说，就是有点小瞧这一类题目，练习的不够多，真的遇到这类题的时候，解题速度慢，
# 效率低。
# 这回我在这里根据别人的答案，总结一下这类题的解题方法。
# 1 最上面本题的答案，中序遍历，在recur的时候更改pre值，这一点非常巧妙
# 2 另一种解法，动态维护leftmax 和rightmin，把这两个值作为函数的参数，动态更新计算。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        leftmax = - float('inf')
        rightmin = float('inf')
        # 2, use pure min, max interval
        def valid(node, leftmax, rightmin):
            if node == None: return True
            if leftmax >= node.val or rightmin <= node.val : return False
            if not valid(node.left, leftmax, node.val): return False
            if not valid(node.right, node.val, rightmin): return False
            return True
        return valid(root, leftmax, rightmin)

# 这两个solution是我自己参考完答案后自己写的，但感觉还是有些可以改进的地方。
# 对照高票答案，进行一些修改。

# 3. 另一种解法，利用中序遍历，将BST的元素按顺序打印并存入数组中，然后判断生成的数组是否为递增数组
#  这种方法比较直观，很容易想到，最后只需要将结果再进行一次判断即可，尽管不能再遍历的过程中就产生答案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]: return False
        print(res)
        return True

# 4. 另一种解法，用stack，一般可以用递归来解的问题都可以用stack。
# 本题用stack存储左孩子，然后每次pop都重新存储左孩子序列。 同时在这个过程中记录pre值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack = []
        pre = None
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val: return False
            pre = root
            root = root.right
            
        return True
            
