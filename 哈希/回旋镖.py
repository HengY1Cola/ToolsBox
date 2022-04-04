from _collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) ->int:
        res = 0
        for pointAim in points:
            x0 , y0 = pointAim
            dic = defaultdict(int)  # 生成字典 默认为int
            for point in points:
                x1 , y1 = point
                distance = (x0 - x1)**2 + (y0 - y1)**2  # 两点之间距离
                dic[distance] += 1
            for key in dic:
                ways = dic[key]
                res += ways * (ways - 1)  # 类似握手问题
        return res

testlist = [[0,0] , [1,0] , [2,0]]
print(Solution().numberOfBoomerangs(testlist))