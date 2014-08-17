# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        lst = []
        lst = self.helper(root, lst)
        return lst        

    def helper(self, root, lst):
        if root == None or root == []:
            return []
        else:
            lst =  self.helper(root.left,  lst) # there's no '+' operator
            lst += self.helper(root.right, lst) # but here is, WHY ???
            lst.append(root.val)
            return lst


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
left = TreeNode(2)

root.left = left

S = Solution()
output = S.postorderTraversal(root)
print (output)
