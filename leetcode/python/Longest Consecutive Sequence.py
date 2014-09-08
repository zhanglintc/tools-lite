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
        dikt = {i : False for i in num} # convert list to dictionary, False for not visit

        fin_max = 0 # init the final max as 0, it should be at least 0

        for i in dikt: # traverse the whole dictionary
            if dikt[i] == False: # this item hasn't been visited
                dikt[i] = True # mark as visited
                cur_max = 0 # init current max

                l = i - 1 # the numbers smaller than i
                r = i + 1 # the numbers bigger than i

                while l in dikt and dikt[l] == False: # l in dikt and not visited
                    dikt[l] = True # mark as visited
                    cur_max += 1 # cur_max++
                    l -= 1 # move to next

                while r in dikt and dikt[r] == False: # r in dikt and not visited
                    dikt[r] = True # mark as visited
                    cur_max += 1 # cur_max++
                    r += 1 # move to next

                fin_max = max(fin_max, cur_max + 1) # update fin_max if cur_max is bigger

        return fin_max


