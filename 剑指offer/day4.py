#输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
#假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        else:
            root = pre.pop(0)
            temp = TreeNode(root)
            depth = tin.index(root)
            temp.left = self.reConstructBinaryTree(pre, tin[:depth])
            temp.right = self.reConstructBinaryTree(pre, tin[depth+1:])
        return temp
