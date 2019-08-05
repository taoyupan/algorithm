**问：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。**

  * BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。
 
 
 ---
 
 **二叉查找树（Binary Search Tree），或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。**
 
 


``` python
'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        else:
            root = sequence[-1]
            del sequence[-1]
            lefttree, righttree = [], []
            #  找到左右子树分界点的位置
            splitindex = -1  # 给位置初始化
            for i in range(len(sequence)):
                if sequence[i] < root:
                    lefttree.append(sequence[i])
                    splitindex = i
                else:
                    break
            for i in range(splitindex+1, len(sequence)):
                if sequence[i] > root:
                    righttree.append(sequence[i])
                else:
                    return False
            if len(lefttree) == 1:
                return True
            else:
                # 递归判断左子树
                left = self.VerifySquenceOfBST(lefttree)
            if len(righttree) == 1:
                right = True
            else:
                right = self.VerifySquenceOfBST(righttree)
            return left and right
```
