# Palindrome Partitioning II
# for leetcode problems
# 2014.12.03 by zhanglin

# Problem:
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        fina_lst = []
        self.partition_helper(s, [], fina_lst)
        return min(fina_lst) - 1 # return min length - 1

    def partition_helper(self, s, this_lst, fina_lst):
        if len(s) == 0:
            fina_lst.append(len(this_lst)) # append length to lst

        for i in range(1, len(s) + 1):
            if self.isPartition(s[:i]):
                self.partition_helper(s[i:], this_lst + [s[:i]], fina_lst)

    def isPartition(self, s):
        left  = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left  += 1
            right -= 1

        return True


