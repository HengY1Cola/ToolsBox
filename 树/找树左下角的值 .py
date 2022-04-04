from sys import exit
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        leftValues = []
        rightValues = []
        if not root.left and not root.right:
            return root.val
        else:
            while queue:
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    left, right = node.left, node.right
                    if left:
                        leftValues.append(left.val)
                        queue.append(left)
                    if right:
                        rightValues.append(right.val)
                        queue.append(right)
            return leftValues.pop()

if __name__ == "__main__":
    root = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    root.left = n2
    root.right = n3
    n3.left = n4
    n3.right = n5
    print("Solution = {0}".format(Solution().findBottomLeftValue(root)))