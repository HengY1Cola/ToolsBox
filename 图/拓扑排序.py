def TopologicalSort(G):
    # 创建入度字典
    in_degrees = dict((u, 0) for u in G)
    # 获取每个节点的入度
    for u in G:
        for v in G[u]:
            in_degrees[v] += 1
    # 使用列表作为队列并将入度为0的添加到队列中
    Q = [u for u in G if in_degrees[u] == 0]
    res = []
    # 当队列中有元素时执行
    while Q:
        # 从队列首部取出元素
        u = Q.pop(0)
        # 将取出的元素存入结果中
        res.append(u)
        # 移除与取出元素相关的指向，即将所有与取出元素相关的元素的入度减少1
        for v in G[u]:
            in_degrees[v] -= 1
            # 若被移除指向的元素入度为0，则添加到队列中
            if in_degrees[v] == 0:
                Q.append(v)
    return res


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
    }
    print(TopologicalSort(graph))
