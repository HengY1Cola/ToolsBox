class Solution:
    def towSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}  # 字典
        for index, num in enumerate(nums):
            if target - num not in dictionary:
                dictionary[num] = index  # 创造 数-下标 键值对
            else:
                return [dictionary[target - num], index]  # 题目确定只有一个答案


nums = [2, 7, 11, 15]
target = 9
print(Solution().towSum(nums, target))