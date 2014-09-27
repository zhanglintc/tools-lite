# Permutations
# for leetcode problems
# 2014.09.23 by zhanglin

# Problem:
# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

# See Combinations.py
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        fina_lst = []

        if len(num) == 1:
            return [num]

        for i in range(len(num)):
            num[i], num[-1] = num[-1], num[i]
            FixNum = num.pop()

            for SortedList in self.permute(num):
                fina_lst.append([FixNum] + SortedList)

            num.append(FixNum)
            num[i], num[-1] = num[-1], num[i]

        return fina_lst
        

s = Solution()
print s.permute([1,2,3])
