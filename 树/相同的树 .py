class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p != None and q != None:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False

root1 = TreeNode(1)
n12 = TreeNode(2)
n13 = TreeNode(3)
n14 = TreeNode(4)
n15 = TreeNode(5)
root1.left=n12
root1.rigth=n13
n12.left=n14
n12.rigth=n15

root2 = TreeNode(1)
n22 = TreeNode(2)
n23 = TreeNode(3)
n24 = TreeNode(4)
n25 = TreeNode(5)
root2.left=n22
root2.rigth=n23
n23.left=n24
n23.rigth=n25

print(Solution().isSameTree(root1, root2))