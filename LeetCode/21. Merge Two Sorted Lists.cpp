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

// corner case -> empty list
// One empty and other non-empty
// both single element
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {

        // Checking all 3 corner cases

        if (list1 == nullptr || list2 == nullptr) {
            if (list1 == nullptr && list2 == nullptr) {
                return nullptr;
            }
            if (list1 == nullptr) {
                return list2;
            }
            return list1;
        }

        ListNode* head;
        if (list1->val < list2->val) {
            head = list1;
            list1 = list1->next;
        } else {
            head = list2;
            list2 = list2->next;
        }

        auto combined_head = head;
        while (list2 != nullptr && list1 != nullptr) {
            if (list1->val <= list2->val) {
                head->next = list1;
                list1 = list1->next;
                head = head->next;
            } else {
                head->next = list2;
                list2 = list2->next;
                head = head->next;
            }
        }

        if (list1 != nullptr) {
            head->next = list1;
        } else {
            head->next = list2;
        }

        return combined_head;
    }
};