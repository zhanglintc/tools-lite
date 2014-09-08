# Longest Consecutive Sequence
# for leetcode problems
# 2014.09.08 by zhanglin

# Problem:
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if num == []:
            return 0

        fin_max = 1
        cur_max = 1

        for i in num:
            l = i - 1
            r = i + 1

            while l in num:
                cur_max += 1
                fin_max = max(fin_max, cur_max)
                while l in num:
                    num.remove(l)
                l -= 1

            while r in num:
                cur_max += 1
                fin_max = max(fin_max, cur_max)
                while r in num:
                    num.remove(r)
                r += 1

            while i in num:
                num.remove(i)
            cur_max = 1

        return fin_max

