from _collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k) -> list[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        res = []
        for numbers in range(2):
            res.append(list[numbers][0])
        return res


nums = [1, 1, 1, 2, 2, 3]
test = Solution().topKFrequent(nums,2)
print(test)