# dijkstra 算法
import heapq

def dijkstra_algorithm(graph, start, end):
    # 堆里的数据都是 (cost, i) 其含义是“从 start 走到 i 的距离是 cost”。
    heap = [(0, start)]
    list = []
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        list.append(u)
        if u == end:
            return [cost, list]
        for v, c in graph[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))
    return -1


if __name__ == '__main__':
    NodeList = ["A", "B", "C", "D", "E", "F"]
    Graph = {
        "A": [["B", 1], ["E", 5], ["D", 4]],
        "B": [["E", 4]],
        "C": [["B", 6], ["F", 6]],
        "D": [["C", 4]],
        "E": [["D", 2]],
        "F": [["A", 2], ["E", 3]],
    }
    for Node in NodeList:
        Distance = dijkstra_algorithm(Graph, "A", Node)
        print("最短距离为："+str(Distance[0])+"  路径为："+str(Distance[1]))
