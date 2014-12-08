# Reverse Nodes in k-Group
# for leetcode problems
# 2014.12.08 by zhanglin

# Problem:
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        p = head
        length = 0

        while p:
            length += 1
            p = p.next

        dummy_head = ListNode(0)
        dummy_head.next = head
        last = dummy_head # always point position n * k - 1

        while length >= k:
            headPrev = last
            headNext = head.next

            idx = 1
            while idx < k:
                head.next = headPrev
                headPrev = head
                head = headNext
                headNext = headNext.next
                idx += 1

            head.next = headPrev
            last.next.next = headNext
            tmp = last.next
            last.next = head

            # reset
            last = tmp
            headPrev = last
            head = tmp.next
            if head:
                headNext = head.next

            length -= k

        return dummy_head.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


s = Solution()
head = s.reverseKGroup(head, 5)

print head.val
print head.next.val
print head.next.next.val
print head.next.next.next.val
print head.next.next.next.next.val

