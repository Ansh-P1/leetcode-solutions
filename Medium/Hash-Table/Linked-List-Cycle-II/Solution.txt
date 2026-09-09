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
    ListNode *detectCycle(ListNode *head) {
        unordered_map<ListNode*, int> v;
        ListNode* temp = head;
        while (temp != NULL){
            if (v.count(temp)){
                return temp;
                //ListNode* ans = temp;
                //ListNode* a= temp
                //return count;
                
            }
            else {
                v[temp] =1;
            }
            temp = temp-> next;
        }
        return NULL;
        
    }
};