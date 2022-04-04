def shellSort(list):
    length = len(list)
    gap = length // 2
    while gap >= 1:
        for i in range(length):
            j = i
            while j >= gap and list[j - gap] > list[j]:  # 在每一组里面进行直接插入排序
                list[j], list[j - gap] = list[j - gap], list[j]
                j -= gap
        gap = gap // 2  # 更新步长
    return list


if __name__ == '__main__':
    list = [5, 3, 2, 6, 8, 7]
    res = shellSort(list)
    print(res)
