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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        ListNode* head = new ListNode();//dummy
        //head->next = actual start point

        ListNode* curr = head;

        //4,5
        //1,3,4
        //2,6
        while(true){

            int min_idx = -1;
            int min_val = 100000;
            for(int i = 0; i < lists.size(); i++){
                if(lists[i] != nullptr && lists[i]->val < min_val){
                    min_val = lists[i]->val; 
                    min_idx = i;            
                }
            }
            if(min_idx == -1)break;
            curr->next = lists[min_idx];  
            curr = curr->next;   
            lists[min_idx] = lists[min_idx]->next;
        }

        return head->next;
    }
};