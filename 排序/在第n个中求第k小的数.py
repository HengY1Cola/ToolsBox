def quickSort(list, start, end, key):
    pivot = list[start]
    right = end
    left = start
    while left < right:
        while left < right and list[right] >= pivot:
            right -= 1
        list[left] = list[right]
        while left < right and list[left] <= pivot:
            left += 1
        list[right] = list[left]
    list[left] = pivot
    if left < right:
        if left-right+1 == key:
            return key
        elif (left-right+1) > key:
            return quickSort(list, start, left-1, key)
        else:
            return quickSort(list, left+1, end, key-(left-start+1))

if __name__ == '__main__':
    li = [5, 3, 2, 6, 8, 7]
    print(li)
    m = int(input('想求第几小的数\n'))
    quickSort(li, 0, len(li) - 1, m-1)
    print(li)
    print(li[m-1])

