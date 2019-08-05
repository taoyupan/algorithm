二叉树的知识点：
=
  1、非空二叉树第i层中至多有2^i个节点（i>=0）<br>
  2、高度为h的二叉树至多有2^{h+1}-1 个节点 <br>
  3、n个节点的完全二叉树树高度h=log2^{n}， 即为不大于log2^{n}的最大整数 <br>

------

完全二叉树的性质：
= 
## 如果n个节点的完全二叉树的节点按层次并按从左到右的顺序从0开始编号，对任意一节点i(0<=i<=n-1)，都有
  * 序号为0的节点是根节点
  * 对于i>0，其父节点的编号为 (i-1)/2 , 要向下取整
  * 若2*1+1<n，其左子节点的序号为2*i+1, **否则** 它无左子节点
  * 若2*i+2<n，其右子节点的序号为2*i+2，**否则** 它无右子节点




**前序遍历 (根-左-右)** <br>
**中序遍历 (左-根-右)** <br>
**后序遍历 (左-右-根)** <br>

```ruby 
class Nnode(object):
    # 节点类
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None
        

class Tree(object):
    def __init__(self):
        self.root = None   # 根节点
    
    def add(self, item):
        # 向树中添加节点生成二叉树
        node = Nnode(item)
        queue = []   #  用队列来存储数据
        queue.append(self.root)
        if self.root is None:
            self.root = node
            return 
        while queue:  # 当队列不为空
            cur_node = queue.pop(0)   # 从对头读取元素
            if cur_node.lchild is None:
                cur_node.lchild = node
                return 
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return 
            else:
                queue.append(cur_node.rchild)
    
    def breadth_trave(self):
        # 层次遍历
        if self.root is None:
            return 
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end= ' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    
    def prior_trave(self,node):
        '''先序遍历（根-左-右）递归'''
        if node is None:
            return
        print(node.elem, end=' ')
        self.prior_trave(node.lchild)
        self.prior_trave(node.rchild)

    def inorder(self,node):
        '''中序遍历(左-根-右)递归'''
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem,end=' ')
        self.inorder(node.rchild)

    def postorder(self,node):
        '''后序遍历(左-右-根)递归'''
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem,end=' ')
        

if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    # tree.breadth_trave()
    # print('')
    tree.prior_trave(tree.root)
    print('')
    # tree.inorder(tree.root)
    # print('')
    # tree.postorder(tree.root)



----



[python实现二叉树的遍历](https://blog.csdn.net/qq_17753903/article/details/82628228)


