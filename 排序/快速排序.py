def quickSort(list, start, end):
    '''
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。 
    '''
    if start >= end:
        return  # 退出递归
    pivot = list[start]
    right = end
    left = start
    while left < right:
        while left < right and list[right] > pivot:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] < pivot:
            left += 1
        list[right] = list[left]
    list[left] = pivot

    quickSort(list, left + 1, end)  # 对右边排序
    quickSort(list, start, left - 1)  # 对左边排序

    '''
    指针思想
    关键点在于start,end
    left,right 两个双指针的运用
    '''


if __name__ == '__main__':
    li = [6, 7, 5, 3, 4, 1, 8]
    quickSort(li, 0, len(li) - 1)
print(li)