/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        if (head->next == NULL){
            return NULL;
        }
        while(fast != NULL && fast->next != NULL){
            fast = fast->next->next;
            if (fast != NULL && fast->next != NULL){
                slow = slow->next;
            }
        }
        ListNode* del = slow->next;
        slow->next = slow->next->next;
        delete del;
        
        return head;  
    }
};