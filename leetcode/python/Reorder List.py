#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reorder List
# for leetcode problems
# 2014.08.17 by zhanglin

# Problem:
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You must do this in-place without altering the nodes' values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None:
            return head
        stack = []
        current = head.next
        while current != None:
            stack.append(current)
            current = current.next

        current = head
        switch = 0
        while stack != []:
            if switch & 0x01:
                current.next = stack.pop(0)
            else:
                current.next = stack.pop()
            current = current.next
            switch += 1

        current.next = None

        return head


