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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int list_size = 0;

        auto temp_head = head;

        while(temp_head != nullptr){
            list_size++;
            temp_head = temp_head->next;
        }
        int traverse = list_size - n;

        if(traverse == 0){
            auto tmp = head;
            return head->next;
        }

        ListNode* pre = nullptr;
        ListNode* cur = head;

        while(traverse--){
            pre = cur;
            cur = cur->next;
        }
        pre->next = cur->next;
        delete cur;



        return head;
    }
};