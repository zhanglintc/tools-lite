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
        before_reverse = dummy_head

        if m == n:
            return head

        idx = 1
        while idx < m:
            head = head.next
            before_reverse = before_reverse.next
            idx += 1

        p_prev = before_reverse
        p_this = head
        p_next = head.next

        while idx <= n and p_next:
            p_this.next = p_prev
            p_prev = p_this
            p_this = p_next
            p_next = p_next.next
            idx += 1

        before_reverse.next.next = p_next
        before_reverse.next = p_this
        p_this.next = p_prev

        return dummy_head.next

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
head.next = ListNode(5)

s = Solution()
head = s.reverseBetween(head, 1, 2)

print head.next.next

