#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reverse Linked List II
# for leetcode problems
# 2014.11.26 by zhanglin

# Problem:
# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        last = dummy_head # always point position m - 1

        idx = 1

        # find beginning
        while idx < m:
            head = head.next
            last = last.next
            idx += 1

        # set the three pointer
        headPrev = last
        headNext = head.next

        # find the end, make head point to position n
        while idx < n:
            head.next = headPrev
            headPrev = head
            head = headNext
            headNext = headNext.next
            idx += 1

        # reconnect three linked list
        head.next = headPrev
        last.next.next = headNext
        last.next = head

        return dummy_head.next


