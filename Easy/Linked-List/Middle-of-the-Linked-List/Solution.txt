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
    ListNode* middleNode(ListNode* head) {
        ListNode* temp = head;
        int count =0;
        while(temp!=NULL){
            count++;
            temp = temp-> next;
        }
        int a=-1;
        if (count % 2 ==0){
            temp = head;
            int cnt =0;
            while(temp!=NULL){
                cnt++;
                if (cnt == count/2){
                    return temp->next;
                }
                temp = temp-> next;
            }
        }
        else {
            temp = head;
            int cnt =0;
            while(temp!=NULL){
                cnt++;
                if (cnt == count/2+1){
                    return temp;
                }
                temp = temp-> next;
            }
        }
        return NULL;
    }
};