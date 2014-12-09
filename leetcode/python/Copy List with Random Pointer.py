# Copy List with Random Pointer
# for leetcode problems
# 2014.12.09 by zhanglin

# Problem:
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.

# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head

        # step 1, add new node to each oldN node
        pt = head
        while pt:
            newNode = RandomListNode(pt.label)
            newNode.next = pt.next
            pt.next = newNode
            pt = pt.next.next

        # step 2, set each new node's random pointer
        pt = head
        while pt:
            if pt.random:
                pt.next.random = pt.random.next
            else:
                pt.next.random = None

            pt = pt.next.next

        # step 3, separate two lists
        newHead = head.next
        ptOld = head
        ptNew = newHead

        while ptNew.next:
            ptOld.next = ptOld.next.next
            ptOld = ptOld.next
            ptNew.next = ptNew.next.next
            ptNew = ptNew.next
            
        ptOld.next = None
        ptNew.next = None

        # return result
        return newHead


