class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mirror(self, root: TreeNode):
        if not root:
            return
        else:
            mirrorNode = TreeNode(root.val)
            mirrorNode.left = self.mirror(root.right)
            mirrorNode.right = self.mirror(root.left)
        return mirrorNode

    def DFS(self, root:TreeNode):
        array = []
        result = []
        if not root:
            return result
        array.append(root)
        while array:
            newNode = array.pop(0)
            result.append(newNode.val)
            if newNode.left != None:
                array.append(newNode.left)
            if newNode.right != None:
                array.append(newNode.right)
        return result


if __name__ == "__main__":
    nums = []
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    root.left = n2
    root.right = n3
    n2.left = n4
    n2.right = n5
    print(Solution().DFS(root))
    test = Solution().mirror(root)
    print(Solution().DFS(test))


