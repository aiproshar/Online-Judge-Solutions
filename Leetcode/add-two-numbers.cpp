//Just traverse and add and push to answer linked list
//Edge Cases [5,0],[5,0] - both traverse nullpointer but you have carry to push in answer linked list
//O(max(m,n)) - Linear Complexity
//There is a stupid loop, we cant initiate without a value and we cant have value if we dont initiate. Just discard the first node (:P)
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *current = new ListNode();
        ListNode *head = current;
        int temp = 0;
        while(l1 != nullptr || l2 != nullptr || temp)
        {
            int add = (l1 == nullptr ? 0 : l1->val) + (l2 == nullptr ? 0 : l2->val) + temp;
            current->next = new ListNode(add % 10);
            current = current->next;
            temp = add > 9 ? 1 : 0;
            l1 = l1 == nullptr ? l1 : l1->next;
            l2 = l2 == nullptr ? l2 : l2->next;   
        }
        return  head->next;
    }
};
//Heh heh boy we are smart we write clean short code 
//FAANG aint daddy boys