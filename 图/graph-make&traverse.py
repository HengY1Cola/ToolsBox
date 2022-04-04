import collections
class VertexNode(object):   # 顶点节点
    def __init__(self, vertexName, visited=False, p=None):
        self.vertexName = vertexName  # 节点名字
        self.Visited = visited        # 此节点是否被访问过
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

    def DFS(self, i):
        self.vertexList[i].Visited = True
        result = self.vertexList[i].vertexName+' '
        p = self.vertexList[i].firstNode
        while(p != None):
            if self.vertexList[p.Index].Visited==True:
                p = p.Next
            else:
                result += self.DFS(p.Index)
        return result

    def DFStravel(self, start):
        i = self.GetIndex(start)
        if i != -1:
            for j in range(self.vertexCount):
                self.vertexList[j].Visited = False
            DFSresult = self.DFS(i)
        return DFSresult

    def BFStravel(self, start):
        BFSresult = ''
        whole = []
        i = self.GetIndex(start)
        if i != -1:
            for j in range(self.vertexCount):
                self.vertexList[j].Visited = False  # 开始遍历 全部设置为flase
                whole.append(j)  # 留着来更新非连通图
            self.vertexList[i].Visited = True  # 第一个为true
            BFSresult += self.vertexList[i].vertexName + ' '
            GList = collections.deque([i])  # 记录遍历顺序
            while GList:
                Node = GList.popleft()
                p = self.vertexList[Node].firstNode
                while p != None:
                    k = p.Index
                    if (self.vertexList[k].Visited == False):
                        self.vertexList[k].Visited = True  # 更改状态
                        BFSresult += self.vertexList[k].vertexName + ' '
                        GList.append(p.Index)
                    p = p.Next
            return BFSresult


if __name__ == '__main__':
    GraphText = Graph()
    vertex_list = ['A', 'B', 'C', 'D', 'E']
    GraphText.InitList(vertex_list)
    GraphText.AddEdge('A', 'C', 0)
    GraphText.AddEdge('A', 'D', 0)
    GraphText.AddEdge('B', 'D', 0)
    GraphText.AddEdge('B', 'E', 0)
    GraphText.AddEdge('C', 'A', 0)
    GraphText.AddEdge('C', 'E', 0)
    GraphText.AddEdge('D', 'A', 0)
    GraphText.AddEdge('D', 'B', 0)
    GraphText.AddEdge('E', 'B', 0)
    GraphText.AddEdge('E', 'C', 0)
    print(GraphText)

    print(GraphText.BFStravel('A'))
    print(GraphText.DFStravel('A'))