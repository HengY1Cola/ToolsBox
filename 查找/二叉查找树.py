class BTNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
 
 
class BTree:
    def __init__(self, root):
        self.root = root;
 
    def insert(self, value):
        self.insertNode(value, self.root)
 
    def insertNode(self, data, btnode):
        if btnode == None:
            btnode = BTNode(data, None, None)
        elif data < btnode.data:
            if btnode.left == None:
                btnode.left = BTNode(data, None, None)
                return
 
            self.insertNode(data, btnode.left)
        elif data > btnode.data:
            if btnode.right == None:
                btnode.right = BTNode(data, None, None)
                return
 
            self.insertNode(data, btnode.right)
 
    def printBTreeImpl(self, btnode):
        if btnode == None:
            return
 
        self.printBTreeImpl(btnode.left)
        print(btnode.data)
        self.printBTreeImpl(btnode.right)
 
    def printBTree(self):
        self.printBTreeImpl(self.root)
 
 
if __name__ == '__main__':
    # 来自csdn 经验证是正确的
    root = BTNode(2, None, None)
    btree = BTree(root)
    for i in [5, 8, 3, 1, 4, 9, 0, 7]:
        btree.insert(i)
 
    btree.printBTree()

  