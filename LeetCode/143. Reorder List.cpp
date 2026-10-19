

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


 //HashMapUh
class Solution {
public:
    void reorderList(ListNode* head) {

        vector<ListNode*> vec;


        auto current = head;

        while(current != nullptr){
            vec.emplace_back(current);
            current = current->next;
        }
        vector<ListNode*> reordered_vec;
        for(int i = 0, j = vec.size()-1; i <= j; i++, j--){
            reordered_vec.emplace_back(vec[i]);
            if(i != j)reordered_vec.emplace_back(vec[j]);
        }
        reordered_vec.emplace_back(nullptr);
        for(int i = 0; i < reordered_vec.size() -1; i++){
            reordered_vec[i]->next = reordered_vec[i+1];
        }
    }
};