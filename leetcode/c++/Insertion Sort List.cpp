/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
    ListNode *insertionSortList(ListNode *head)
    {
        ListNode *new_head = new ListNode(0);
        ListNode *pt_cache = NULL;
        ListNode *pt_currt = NULL;

        if(head == NULL || head->next == NULL)
        {
            return head;
        }

        while(head != NULL)
        {
            if(new_head->next == NULL)
            {
                new_head->next = head;
                head = head->next;
                new_head->next->next = NULL;
            }
            else
            {
                pt_cache = new_head;
                pt_currt = new_head->next;

                while(pt_currt != NULL)
                {
                    if(head->val <= pt_currt->val)
                    {
                        pt_cache->next = head;
                        head = head->next;
                        pt_cache->next->next = pt_currt;
                        break;
                    }
                    else
                    {
                        pt_cache = pt_cache->next;
                        pt_currt = pt_currt->next;
                        continue;
                    }
                }

                if(pt_currt == NULL)
                {
                    pt_cache->next = head;
                    head = head->next;
                    pt_cache->next->next = NULL;
                }
            }
        }
        return new_head->next;
    }
};