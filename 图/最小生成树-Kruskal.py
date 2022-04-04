from typing import List, Tuple
'''
Kruskal 加边法
'''


def kruskal(num_nodes: int, edges: List[Tuple[int, int, int]]) -> int:

    edges = sorted(edges, key=lambda edge: edge[2])  # 对边进行排序
    parent = list(range(num_nodes))  # 将 n 个顶点初始化为 n 个联通域

    def find_parent(i):
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        return parent[i]

    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []

    for edge in edges:
        parent_a = find_parent(edge[0])
        parent_b = find_parent(edge[1])
        if parent_a != parent_b:
            minimum_spanning_tree_cost += edge[2]
            minimum_spanning_tree.append(edge)
            parent[parent_a] = parent_b

    return minimum_spanning_tree


if __name__ == "__main__":
    num_nodes = 4
    num_edges = 5
    edges = [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)]
    kruskal(num_nodes, edges)
    print(kruskal(num_nodes, edges))