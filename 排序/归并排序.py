def merge_sort(alist):
    n=len(alist)
    if n <= 1:
        return alist
    mid = n//2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    list = [10, 1, 18, 30, 223, 12, 7, 5, 18, 17]
    print("排序前：" + str(list))
    print("排序后：" + str(merge_sort(list)))