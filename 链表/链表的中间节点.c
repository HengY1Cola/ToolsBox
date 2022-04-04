# 创建节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 创建单链表类
class SingleLinkList(object):
    def __init__(self):
        self.header = None
        self.length = 0

    # 1、判断是否为空
    def is_empty(self):
        if self.header == None:
            return True
        else:
            return False

    # 2、头部插入
    def add(self, node):
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
            # currentNode = self.header
        self.length += 1

    # 3、尾部插入
    def append(self, node):
        current_Node = self.header
        if self.is_empty():
            self.add(node)
        else:
            while (current_Node.next != None):
                current_Node = current_Node.next
            current_Node.next = node
            self.length += 1

class Solution:
    def middleNode(self,list:SingleLinkList) -> Node:
        slow = fast = list.header
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



list = SingleLinkList()
list.append(Node(1))
list.append(Node(2))
list.append(Node(3))
list.append(Node(4))
res = Solution().middleNode(list)
print(res.data)