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
        before_reverse = dummy_head

        idx = 1
        while idx != m:
            head = head.next
            before_reverse = before_reverse.next
            idx += 1

        pre_in_reverse = head
        while idx != n:
            pass

        return dummy_head.next


