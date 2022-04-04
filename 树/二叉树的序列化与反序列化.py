class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, root: TreeNode):
        if not root:
            return "null"
        else:
            queue = []
            queue.append(root)
            res = ""
            while queue:
                node = queue.pop(0)
                if node:
                    res += str(node.val)+","
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res += "null,"
            return res

    def deserialize(self, data) ->TreeNode:
        if not data:
            return None
        else:
            data = data.split(",")
            root = TreeNode(data.pop(0))
            queue = []
            queue.append(root)
            while queue:
                node = queue.pop(0)
                if data:
                    val = data.pop(0)
                    if val != "null":
                        node.left = TreeNode(val)
                if data:
                    val = data.pop(0)
                    if val != "null":
                        node.right = TreeNode(val)
            return root

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
print(Solution().serialize(root))
str="1,2,3,4,5,null,null,null,null,null,null"
test = Solution().deserialize(str)
print(test.left.val)
print(test.right.val)