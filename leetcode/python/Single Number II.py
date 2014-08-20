# Single Number II
# for leetcode problems
# 2014.08.20 by zhanglin

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        times = {}
        for i in A:
            if i not in times:
                times[i] = 1
            else:
                times[i] += 1

        for key, val in times.items():
            if val == 1:
                return key

input = [1,1,11,11]
S = Solution()
print(S.singleNumber(input))
