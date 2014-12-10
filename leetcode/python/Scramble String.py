# Scramble String
# for leetcode problems
# 2014.12.10 by zhanglin

# Problem:
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True

        if len(s1) == 2:
            if s1[0] == s2[1] and s1[1] == s2[0]:
                return True

        for i in range(1, len(s1) - 1):
            if self.count(s1[:i]) == self.count(s2[:i]) and self.count(s1[i:]) == self.count(s2[i:]):
                return True

        return False

    def count(self, string):
        times = {}

        for ch in string:
            if ch not in times:
                times[ch] = 0

            else:
                times[ch] += 1

        return times

s = Solution()
print s.isScramble('abb', 'bab')

print 'abb'[:2]
print 'abb'[2:]
