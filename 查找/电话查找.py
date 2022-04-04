import copy


class VertexNode(object):   # 顶点节点
    def __init__(self, begin: int, p=None):
        self.begin = begin
        self.next = p


class EdgeNode(object):  # 边节点
    def __init__(self, num, name, p=None):
        self.num = num
        self.name = name
        self.next = p


class Graph(object):  # 邻接表存储图的结构
    def __init__(self, count=0):
        self.List = []   # 用list连接边表
        self.Count = count

    def InitList(self, List):  # 初始化
        for Num in List:
            self.List.append(VertexNode(Num))
        self.Count = len(List)

    def GetIndex(self, begin):
        for i in range(self.Count):
            temp = self.List[i].begin
            if (temp is not None) and (begin == temp):
                return i
        return -1

    def AddEdge(self, num, name):  # 添加信息
        begin = int(str(num)[:3])
        i = self.GetIndex(begin)
        if i == -1:
            print("不存在")
        else:
            temp = self.List[i].next
            if not temp:
                self.List[i].next = EdgeNode(num, name)
            else:
                while temp.next is not None:
                    temp = temp.next
                temp.next = EdgeNode(num, name)
    def Gather(self):
        list = []
        for x in range(self.Count):
            while self.List[x].next is not None:
                list.append(self.List[x].next)
                self.List[x].next = self.List[x].next.next
        return list


if __name__ == '__main__':
    GraphText = Graph()
    beginList = [133, 149, 153, 177, 156]
    beginList.sort()
    GraphText.InitList(beginList)  # 头节点
    GraphText.AddEdge(13354430923, '黄华健')
    GraphText.AddEdge(13343209890, '李俊杰')
    GraphText.AddEdge(14954319870, '杨江逸')
    GraphText.AddEdge(14945397890, '高尚滔')
    GraphText.AddEdge(15354809733, '旷华宇')
    GraphText.AddEdge(15354309574, '钱家梁')
    GraphText.AddEdge(15354309574, '梁铭杰')
    GraphText.AddEdge(15623409987, '吴国浩')
    GraphText.AddEdge(15654329807, '招达雄')
    GraphText.AddEdge(17753419801, '王彤')
    GraphText.AddEdge(17734598021, '苏晓雯')
    # for x in GraphText.List:
    #     print(type(x.begin))
    print('菜单：')
    print('按1 根据名字查电话：')
    print('按2 根据电话查名字：')
    m = input('请输入：')
    flag = 'r'
    m = int(m)
    if m == 1:
        allList = GraphText.Gather()
        while flag != 'q':
            name = input('请输入名字：\n')
            num = None
            for x in allList:
                if x.name == name:
                    num = x.num
                    print(num)
            if num is None:
                print('不存在')
            flag = input('按任意键继续，若需退出请输入q')
    if m == 2:
        while flag != 'q':
            num = input('请输入电话：\n')
            num = int(num)
            begin = int(str(num)[:3])
            name = None
            for x in GraphText.List:
                if x.begin == begin:
                    index = GraphText.GetIndex(begin)
                    while GraphText.List[index].next is not None:
                        if GraphText.List[index].next.num == num:
                            name = GraphText.List[index].next.name
                            print(name)
                            break
                        else:
                            GraphText.List[index].next = GraphText.List[index].next.next
            if name is None:
                print('不存在')
            flag = input('按任意键继续，若需退出请输入q')
    print("感谢使用")