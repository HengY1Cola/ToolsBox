class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode):
        self.res = []
        def dfs(root, row, col):
            if not root:
                return
            else:
                self.res.append([root.val, row, col])
                dfs(root.left, row+1, col-1)
                dfs(root.right, row+1, col+1)
        dfs(root, 0, 0)
        self.res.sort(key=lambda x: (x[2], x[1], x[0]))
        resAll = [[self.res[0][0]]]
        for i in range(1, len(self.res)):
            if self.res[i][2] == self.res[i - 1][2]:
                resAll[-1].append(self.res[i][0])
            else:
                resAll.append([self.res[i][0]])
        return resAll

if __name__ == "__main__":
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    print(Solution().verticalTraversal(root))