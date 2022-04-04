try:
    num = int(input('请输入一个数字: -1结束\n'))
except:
    print('请输入正确的整数')
list = []
while num != -1:
    list.append(num)
    try:
        num = int(input('请输入一个数字: -1结束\n'))
    except:
        print('请输入正确的整数')
        break
print(list)
try:
    num = int(input('请输入查找数字:\n'))
except:
    print('请输入整数')
indexlist = []
for x in range(len(list)):
    if list[x] == num:
        indexlist.append(x+1)

if indexlist == []:
    print('没有匹配项目')
else:
    print(indexlist)




