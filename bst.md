# Binary Search Tree (BST)
这里整理专门做一个bst的专题整理。之前没有针对bst做过专项训练，因为觉得这类题目无非就是递归，没啥难度，谁知道真的做类似的题目的时候，思路来的并不快。
所以，我觉得有必要做一个专项训练梳理一下。

## 中序，前序，后序， ldr, rdl, dlr, drl, lrd, rld
其实就是左，中，右进行排列组合，针对题目的需求选择对应的遍历方法。

## bst的一些基本性质
1. bst本身进行中序遍历就可以得到有序数列。
2. 可以用pre变量记录中序遍历过程中的previous node，它是当前遍历节点的前继节点。
3. 在进行递归的时候，可以进行一些变化，可以在递归函数中加入一些变量，比如leftmax, rightmin
4. 递归的问题都可以用stack来模拟解决。

## 相关题目
- 98 validate binary search tree. 主要是要考虑到如何动态计算存储左右边界. 或者存储pre
- 530 Minimum Absolute Difference in BST. 中序遍历，存储pre
- 700. Search in a Binary Search Tree. 
	这道很基础的easy题，之前压根没有思考过，今天写了一下，不是最优的，因为搜索的时候同时遍历左右子树。没有考虑到bst的属性，搜索只需要O(log(n))
- 701. Insert into a Binary Search Tree
	这一题其实也不难，但是我写的不是最优解，额外写了个helper函数，不够简洁
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        self.parent = root
        
        def searchinsert(root, val):
            if not root: 
                temp = TreeNode(val)
                if self.parent.val < val:
                    self.parent.right = temp
                else:
                    self.parent.left = temp
            elif root.val < val:
                self.parent = root
                searchinsert(root.right, val)
            else:
                self.parent = root
                searchinsert(root.left, val)
            
        
        searchinsert(root, val)
        return root
```

```python
## 参考了一下别人的方法，把代码重新精简一下
class Solution(object):
    def insertIntoBST(self, root, val):
        if(root == None): return TreeNode(val);
        if(root.val < val): root.right = self.insertIntoBST(root.right, val);
        else: root.left = self.insertIntoBST(root.left, val);
        return(root)

这里面首先不需要一个parent来存储，直接就将返回值符给子节点。 非常巧妙

```

