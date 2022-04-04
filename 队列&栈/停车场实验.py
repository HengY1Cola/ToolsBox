class car:
    def __init__(self, num: int, arrivetime=0, leftime=0):
        self.num = num
        self.arrivetime = arrivetime
        self.leftime = leftime

class Solution:
    def carIn(self, carlist: list) ->list:
        carnum = input('请输入车号:例如001\n')
        num = int(carnum)
        if num in container:
            print('抱歉，存在该辆车')
            return carlist
        else:
            carArrivetime = input('请输入到达时间，例如：5\n')
            carArrivetimeNum = int(carArrivetime)
            oneCar = car(num, carArrivetimeNum)
            carlist.append([oneCar.num, oneCar.arrivetime])
            print("这辆车已经停进去啦\n")
            container.append(num)
            return carlist

    def carOut(self, carlist: list) ->list:
        carLocation = input('请输入车位号\n')
        carlLefTime = input('请输入离开的时间\n')
        carLocationNum = int(carLocation)
        carlLefTimeNum = int(carlLefTime)
        output = []
        while len(carlist) > carLocationNum:
            output.append(carlist.pop())
        res = carlist.pop()
        while len(output) > 0:
            carlist.append(output.pop())
        if carlLefTimeNum >= int(res[1]):
            money = (carlLefTimeNum - int(res[1]))
            print('需要交'+str(money)+'元\n')
            return carlist
        else:
            print("系统错误\n")
            return False


print('欢迎使用停车系统\n')
n = input('请输入停车位\n')
seat = int(n)
carList = []
container = []
m = input('停车请输入"A",出库请输入"B",停止请输入"E"\n')
while m != 'E':
    if m == 'A':
        if len(carList) == seat:
            print('该停车位已经满了\n')
        else:
            carList = Solution().carIn(carList)
    elif m == 'B':
        if len(carList) == 0:
            print('没车啦')
        else:
            print(carList)
            carList = Solution().carOut(carList)
    else:
        print("暂时没有这个选项")
    m = input('停车请输入"A",出库请输入"B",停止请输入"E"\n')
print('退出使用')