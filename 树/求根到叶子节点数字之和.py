import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.rigth = right

class SolutionDFS:
    def sumNumbersA(self, root: TreeNode) -> int:
        def DFS(root: TreeNode, prevTotal = 0) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.rigth:
                return total
            else:
                return DFS(root.left, total) + DFS(root.rigth, total)
        return DFS(root)
class SolutionBFS:
    def sumNumbersB(self,root:TreeNode) -> int:
        if not root:
            return 0
        total =0
        nodeQueue = collections.deque([root])
        numQueue = collections.deque([root.val])
        while nodeQueue:
            node, num=nodeQueue.popleft(), numQueue.popleft()
            left, right = node.left, node.rigth
            if not node.left and not node.rigth:
                 total += num
            else:
                if node.left:
                    nodeQueue.append(node.left)
                    numQueue.append(num*10+left.val)
                if node.rigth:
                    nodeQueue.append(node.rigth)
                    numQueue.append(num * 10 + right.val)
        return total

root1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
root1.left = n2
root1.rigth = n3
n2.left = n4
n2.rigth = n5

test1=SolutionDFS().sumNumbersA(root1)
print(test1)

test2=SolutionBFS().sumNumbersB(root1)
print(test2)