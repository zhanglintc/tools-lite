// Balanced Binary Tree
// for leetcode problems
// 2015.03.20 by zhanglin

// Problem:
// Given a binary tree, determine if it is height-balanced.

// For this problem, a height-balanced binary tree is defined as a binary tree
// in which the depth of the two subtrees of every node never differ by more than 1.

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int helper(TreeNode root) {
        if(root == null) {
            return 0;
        }

        int left  = helper(root.left);
        int right = helper(root.right);

        return (left > right ? left : right) + 1;
    }

    public boolean isBalanced(TreeNode root) {
        if(root == null) {
            return true;
        }

        if(Math.abs(helper(root.left) - helper(root.right)) <= 1) {
            return isBalanced(root.left) && isBalanced(root.right);
        }

        else {
            return false;
        }
    }
}


