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
        return min(self.partition_helper(s, 0), self.partition_helper(s[::-1], 0))

    def partition_helper(self, s, cuts):
        for i in range(len(s) + 1, 0, -1):
            if self.isPartition(s[:i]) and i == len(s) + 1:
                return cuts

            elif self.isPartition(s[:i]):
                return self.partition_helper(s[i:], cuts + 1)

            else:
                continue

    def isPartition(self, s):
        left  = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left  += 1
            right -= 1

        return True


s=Solution()
print s.minCut('aaabaa')

