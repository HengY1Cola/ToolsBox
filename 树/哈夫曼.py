from _collections import defaultdict


class Treenode:
    def __init__(self, name=None, value=None, left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right
        self.code = ""


class Solution:
    def huff_man_tree(self, char_weights) -> Treenode:
        if len(char_weights) ==1:
            exit()
        leaves = [Treenode(part[0], part[1]) for part in char_weights]  # 生成叶子结点list
        while len(leaves) != 1:
            leaves.sort(key=lambda x: x.value, reverse=True)  # 以权值进行从大到小排序(必须每次排序)
            c = Treenode(value=(leaves[-1].value + leaves[-2].value))  # 将最后2个进行相加
            c.left = leaves.pop(-1)
            c.right = leaves.pop(-1)
            leaves.append(c)
        root = leaves[0]
        return root
    '''
    对初始化的哈夫曼树进行编码
    如果从该节点向左，则左孩子的编码为该节点编码 + '0’
    如果从该节点向右，则右孩子的编码为该节点编码 + '1’
    '''
    def set_code(self, root: Treenode):
        dicCode = {}
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                node.right.code = node.code + "1"
            if node.left:
                stack.append(node.left)
                node.left.code = node.code + "0"
        stack2 = []
        stack2.append(root)
        while len(stack2) != 0:
            node2 = stack2.pop()
            if node2.name:
                print(node2.name+'   '+node2.code)
                dicCode[node2.name] = node2.code
            if node2.left:
                stack2.append(node2.left)
            if node2.right:
                stack2.append(node2.right)
        return dicCode
    '''
    进行编码
    '''
    def coding(self, str, dic):
        n = len(str)
        res = ""
        for i in range(n):
            for a, b in dic.items():
                if a == str[i]:
                    res += b
        return res
    '''
    进行解码
    '''
    def decode(self, res, dic):
        ret = ''
        while res != '':
            for item, value in dic.items():
                if value in res and res.index(value) == 0:
                    ret += item
                    res = res[len(value):]
        return ret







if __name__ == '__main__':
    list = []
    a = input('请输入字符')  # 得到字符集
    length = len(a)
    for i in range(length):
        list.append(a[i])
    print(list)
    dic = defaultdict(int)
    for str in list:
        dic[str] += 1
    print('得到频率如下')
    print(dic)  # 得到权重的字典
    n = len(dic)  # 字符的种类
    char_weights = []
    for i, j in dic.items():  # 汇集结点和权重
        char_weights.append((i, j))
    print('\n')
    node = Solution().huff_man_tree(char_weights)
    dic = Solution().set_code(node)
    print(dic)
    res = Solution().coding(a, dic)
    print('编码：'+res+' ')
    ret = Solution().decode(res, dic)
    print('解码：'+ret+' ')
    exit()