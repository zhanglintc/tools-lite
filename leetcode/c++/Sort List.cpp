// Sort List
// for leetcode problems
// 2014.08.14 by zhanglin

// Problem:
// Sort a linked list in O(n log n) time using constant space complexity.

/**
 * Definition for singly-linked list->
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *merge(ListNode *left, ListNode *right)
    {
        ListNode *new_head;
        ListNode *pointer;
        
        if(left == NULL)
        {
            return right;
        }
        if(right == NULL)
        {
            return left;
        }
        
        new_head = new ListNode(0);
        pointer = new_head;
        
        while(left != NULL && right != NULL)
        {
            if(left->val < right->val)
            {
                pointer->next = left;
                left = left->next;
            }
            else
            {
                pointer->next = right;
                right = right->next;
            }
            pointer = pointer->next;
        }
        
        if(left == NULL)
        {
            pointer->next = right;
        }
        if(right == NULL)
        {
            pointer->next = left;
        }
        
        return new_head->next;
    }
    
    ListNode *sortList(ListNode *head)
    {
        ListNode *fast;
        ListNode *slow;
        ListNode *new_head_left;
        ListNode *new_head_right;
        
        if(head == NULL || head->next == NULL)
        {
            return head;
        }
        
        fast = head;
        slow = head;
        
        while(fast->next != NULL && fast->next->next != NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        
        new_head_left = head;
        new_head_right = slow->next;
        slow->next = NULL;
        
        new_head_left = sortList(new_head_left);
        new_head_right = sortList(new_head_right);
        
        return merge(new_head_left, new_head_right);
    }
};


