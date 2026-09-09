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
    bool hasCycle(ListNode *head) {
        unordered_set<ListNode*> seen;
        ListNode* temp = head;
        while(temp != NULL){
            ///int a = temp->val;
            if (seen.count(temp)){
                return true;
            }
            else {
                seen.insert(temp);
            }
            temp = temp->next;
        }
        return false; 
    }
};