try:
    num = int(input('请输入不重复数字: -1结束\n'))
except:
    print('错误')
    exit()

list = []
while num != -1:
    if num not in list:
        list.append(num)
        try:
            num = int(input('请输个不重复数字: -1结束\n'))
        except:
            print('请输入正确的整数')
            break
    else:
        print('存在重复数字')
        exit()
print(list)
try:
    num = int(input('请输入查找数字:\n'))
except:
    print('请输入整数')
list.sort()
print('经过排序后：')
print(list)


def find(list, num, left, right):
    mid = int((left+right)/2)
    if(left <= right):
        if num not in list:
            print('不存在')
        elif list[mid] < num:
            result = find(list, num, mid+1, right)
        elif list[mid] > num:
            result = find(list, num, left, mid-1)
        elif list[mid] == num:
            return mid
        return result


print(find(list, num, 0, len(list)-1)+1)
