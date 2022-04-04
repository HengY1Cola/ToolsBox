class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        else:
            res, i, j = 0, 0, 0
            window = set()
            n = len(s)
            while j < n:
                if s[j] not in window:
                    window.add(s[j])
                    res = max(res, j-i+1)  # 前后比较谁更大
                    j += 1
                else:
                    if i < j:
                        window.remove(s[i])
                        i += 1
                    else:
                        j += 1  # 这种是i,j又在一起了
            return res
a ='pwwkew'
test = Solution().lengthOfLongestSubstring(a)
print(test)