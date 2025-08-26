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


//Iterative Solution
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        if(head == nullptr || head->next == nullptr){
            return head;
        }

        auto prev = head;
        auto current = head->next;
        head->next = nullptr;

        while(true){
            if(current->next == nullptr){
                current->next = prev;
                return current;
            }
            auto next = current->next;
            current->next = prev;
            prev = current;
            current = next;

        }

    }
};


//Recursive Solution
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

        if(head == nullptr || head->next == nullptr){
            return head;
        }


        auto prev = head;
        auto current = head->next;
        prev->next = nullptr;
        while(current != nullptr){
            auto next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        return prev;
    }

};