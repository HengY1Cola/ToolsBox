from _collections import defaultdict

'''
1.首先得明白去除后能被k整除相当于sum（list）%k=sum（切除片段）%k，这个就拿下面的例子看看就行 余数为 target
2.所以我们的目的就是找到哪个片段，题意中说了是连续的片段，接下来
3.n*k+a=sum(0:i) 即从第一个到第i个的余数为a
  m*k+b=sum(o:j) 即从第一个到第j个的余数为a
  那么(i:j)就是我们要求得片段 ->  (m-n)*k+(b-a)=sum(i:j)
  即他的余数为(b-a)可能为负 -> (b-a+k)=target
  则a=b-target+k a就是我们要求得
4.运用哈希，将得到得余数作为键存放起来 用i作为值视为位置 i j
'''
class Solution:
    def solve(self, nums: list, k: int) -> int:
        n = len(nums)
        target = sum(nums) % k
        if target == 0:
            return 0
        res = n
        dic = defaultdict(int)
        dic[0] = -1
        presum = 0  # 先前的总合
        for i in range(n):
            presum = (presum + nums[i]) % k
            if (presum - target + k) % k in dic:
                res = min(res, i - dic[(presum - target+k) % k])
            dic[presum] = i
        if res == n:
            return -1
        else:
            return  res




nums = [1, 8, 6, 4, 5]
k = 7
test = Solution().solve(nums,k)
print(test)