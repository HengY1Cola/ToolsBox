import math


def radix_sort(the_list, radix=10):
    i = int(math.ceil(math.log(max(the_list), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, i + 1):
        for val in the_list:
            bucket[int(val % (radix ** i) / (radix ** (i - 1)))].append(val)
        del the_list[:]
        for each in bucket:
            the_list.extend(each)
        bucket = [[] for i in range(radix)]
    return the_list


if __name__ == '__main__':
    list = [10, 1, 18, 30, 223, 12, 7, 5, 18, 17]
    print("排序前：" + str(list))
    print("排序后：" + str(radix_sort(list)))