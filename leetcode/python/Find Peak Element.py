#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Find Peak Element
# for leetcode problems
# 2014.12.07 by zhanglin

# Problem:
# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        num = [None] + num + [None]

        for i in range(1, len(num) - 1):
            if num[i - 1] < num[i] > num[i + 1]:
                return i - 1

        return None


