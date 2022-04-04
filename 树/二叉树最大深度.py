from sys import exit

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.rigth = right

class SolutionA:
    #  最大深度
    def maxDepthA(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth=self.maxDepthA(root.left)
        rigth_depth = self.maxDepthA(root.rigth)
        return max(left_depth, rigth_depth)+1

class SolutionB:
    #  BFS， 使用辅助队列。 每推进一层，深度加一。
    def maxDepthB(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        res = 0
        while queue:
            for _ in range(len(queue)):
                p = queue.pop(0)
                if p.left : queue.append(p.left)
                if p.rigth : queue.append(p.rigth)
            res += 1
        return res
  
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
	print("maxDepthA = {0}".format(root.maxDepthA()))
	print("maxDepthB = {0}".format(root.maxDepthB()))
	exit(0)