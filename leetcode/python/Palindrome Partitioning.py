# Palindrome Partitioning
# for leetcode problems
# 2014.11.30 by zhanglin

# Problem:
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        fina_lst = []
        self.partition_helper(s, [], fina_lst)
        return fina_lst

    def partition_helper(self, s, this_lst, fina_lst):
        if len(s) == 0:
            fina_lst.append(this_lst)

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


