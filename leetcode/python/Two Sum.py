# Two Sum
# for leetcode problems
# 2014.07.04 by zhanglin

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if num[i] in d:
                return (d[num[i]] + 1, i + 1)
            else:
                d[target - num[i]] = i
