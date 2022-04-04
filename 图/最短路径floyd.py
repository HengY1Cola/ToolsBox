# floyd算法


class VertexNode(object):   # 顶点节点
    def __init__(self, name, nickName =None, introduction=None, p=None):
        self.vertexName = name
        self.nickName = nickName
        self.Introduction = introduction
        self.firstNode = p          # 指向所连接的边表节点的指针


class EdgeNode(object):  # 边节点
    def __init__(self, index, weight = 0, p=None):
        self.Index =index   # 尾节点在边表中对应序号
        self.Weight = weight  # 边的权值
        self.Next = p       # 链接同一头节点的下一条边


class Graph(object):  # 邻接表存储图的结构
    def __init__(self, vcount=0):
        self.vertexList = []   # 用list连接边表
        self.vertexCount = vcount

    def InitList(self, VertexList):  # 初始化
        for VertexName in VertexList:
            self.vertexList.append(VertexNode(VertexName))
        self.vertexCount = len(VertexList)

    def GetIndex(self, VertexName):    #获取指定名称节点的序号
        for i in range(self.vertexCount):
            temp = self.vertexList[i].vertexName
            if (temp != None) and (VertexName == temp):
                return i
        return -1

    def AddEdge(self, startNode, endNode, weight):  # 添加边的信息
        i = self.GetIndex(startNode)
        j = self.GetIndex(endNode)
        if i == -1 or j == -1:
            print("不存在该边")
        else:
            weight = float(weight)
            temp = self.vertexList[i].firstNode
            if not temp:  # 若边表下无顶点信息
                self.vertexList[i].firstNode = EdgeNode(j, weight)
            else:  # 若边表下已有顶点信息
                while (temp.Next != None):
                    temp = temp.Next
                temp.Next = EdgeNode(j, weight)


def floyd_warshall(graph, v):
    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

    # check vertex k against all other vertices (i, j)
    for k in range(v):
        # looping through rows of graph array
        for i in range(v):
            # looping through columns of graph array
            for j in range(v):
                if (
                        dist[i][k] != float("inf")
                        and dist[k][j] != float("inf")
                        and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist, v




if __name__ == '__main__':
    GraphText = Graph()  # 实例化
    vertex_list = ['宿舍', '操场', '图书馆', '教室', '食堂']
    GraphText.InitList(vertex_list)  # 初始化
    count = GraphText.vertexCount  # 个数
    GraphText.AddEdge('宿舍', '操场', 6)
    GraphText.AddEdge('宿舍', '食堂', 4)
    GraphText.AddEdge('操场', '教室', 5)
    GraphText.AddEdge('图书馆', '操场', 3)
    GraphText.AddEdge('图书馆', '宿舍', 3)
    GraphText.AddEdge('教室', '宿舍', 6)
    GraphText.AddEdge('教室', '食堂', 2)
    GraphText.AddEdge('教室', '图书馆', 3)
    GraphText.AddEdge('食堂', '图书馆', 2)
    GraphText.AddEdge('操场', '宿舍', 6)
    GraphText.AddEdge('食堂', '宿舍', 4)
    GraphText.AddEdge('教室', '操场', 5)
    GraphText.AddEdge('操场', '图书馆', 3)
    GraphText.AddEdge('宿舍', '图书馆', 3)
    GraphText.AddEdge('宿舍', '教室', 6)
    GraphText.AddEdge('食堂', '教室', 2)
    GraphText.AddEdge('图书馆', '教室', 3)
    GraphText.AddEdge('图书馆', '食堂', 2)  # 添加双向边

    Dormitory = VertexNode("宿舍", "轩和居", "“宿舍”是住宿的房屋，包括寝室、卫生间、洗浴间、阳台等。宿舍住的人数不同，有单人间，双人间，多人间等。")
    Playground = VertexNode("操场", "地平线", "操场是供体育锻炼用的场地，多用指学校进行体育活动和教学活动的专置场地。")
    Library = VertexNode("图书馆", "袖珍城镇", "是搜集、整理、收藏图书资料以供人阅览、参考的机构.")
    Classroom =VertexNode("教室", "博雅舍", "是教师向学生传授课业的场所。")
    Dining = VertexNode("食堂", "不好吃", "指设于机关、学校、厂矿等企事业单位、为供应其内部职工、学生等就餐的场所。")

    G = [[0, 6, 3, 6, 4], [6, 0, 3, 5, float('inf')], [3, 3, 0, 3, 2], [6, 5, 3, 0, 2], [4, float('inf'), 2, 2, 0]]
    res = floyd_warshall(G, 5)

    print('菜单：\n')
    print('查看宿舍请按1：')
    print('查看操场请按2：')
    print('查看图书馆请按3：')
    print('查看教室请按4：')
    print('查看食堂请按5：')
    print('查看最短路径请按6：')
    inputText = input('请输入选项--按q退出')
    while inputText != 'q':
        if inputText == '1':
            print("宿舍的昵称为："+Dormitory.nickName)
            print("宿舍的介绍：" + Dormitory.Introduction)
        elif inputText == '2':
            print("操场的昵称为："+Playground.nickName)
            print("操场的介绍：" + Playground.Introduction)
        elif inputText == '3':
            print("图书馆的昵称为："+Library.nickName)
            print("图书馆的介绍：" + Library.Introduction)
        elif inputText == '4':
            print("教室的昵称为："+Classroom.nickName)
            print("教室的介绍：" + Classroom.Introduction)
        elif inputText == '5':
            print("食堂的昵称为："+Dining.nickName)
            print("食堂的介绍：" + Dining.Introduction)
        elif inputText == '6':
            print("两点的最短距离为："+str(res[0]))
        else:
            print("错误")
        inputText = input('请再次输入选项--按q退出')