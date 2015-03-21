// Balanced Binary Tree
// for leetcode problems
// 2015.03.21 by zhanglin

// Problem:
// Given a binary tree, determine if it is height-balanced.

// For this problem, a height-balanced binary tree is defined as a binary tree
// in which the depth of the two subtrees of every node never differ by more than 1.

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int helper(TreeNode *root) {
        if(root == NULL) {
            return 0;
        }

        int left  = helper(root->left);
        int right = helper(root->right);

        return (left > right ? left : right) + 1;
    }

    bool isBalanced(TreeNode *root) {
        if(root == NULL) {
            return true;
        }

        if(abs(helper(root->left) - helper(root->right)) <= 1) {
            return isBalanced(root->left) && isBalanced(root->right);
        }

        else {
            return false;
        }
    }
};


