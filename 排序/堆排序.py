import random


def makeRootMax(heap, heapSize, root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    '''
    已知某个节点的下标root
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2
    '''
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        # 递归的对子树做调整
        heap[larger], heap[root] = heap[root], heap[larger]
        makeRootMax(heap, heapSize, larger)


def rebuildHeap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heapSize = len(heap)
    for i in range((heapSize - 2)//2, -1, -1):  # 自底向上建堆
        makeRootMax(heap, heapSize, i)


def heapSort(heap):  # 第一个元素与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    rebuildHeap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        makeRootMax(heap, i, 0)


if __name__ == '__main__':
    a = [5, 3, 2, 6, 8, 7]
    heapSort(a)
    print(a)

