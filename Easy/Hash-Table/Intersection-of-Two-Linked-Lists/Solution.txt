/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set <ListNode*> seen;
        ListNode* a = headA;
        ListNode* b = headB;
        while(a != NULL || b != NULL){
            if (seen.count(a)){
                return a;
            }
            else {
                if(a!=NULL){
                    seen.insert(a);
                }
                
            }
            if (seen.count(b)){
                return b;
            }
            else {
                 if(b!=NULL){
                    seen.insert(b);
                }
            }
            if (a != NULL){
                a = a->next;
            }
            if (b != NULL){
                b = b->next;
            }
        }
        return NULL;
        
    }
};