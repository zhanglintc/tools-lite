# Unique Binary Search Trees
# for leetcode problems
# 2014.08.29 by zhanglin

# Problem:
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = {}                     # initialize dictionary Dynamic Plan
        dp[0] = 1                   # special case 1
        dp[1] = 1                   # special case 2
        for i in range(2, n + 1):   # (2, n]
            dp[i] = 0               # initialize dp(i)
            for j in range(0, i):   # (0, i)
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[n]
