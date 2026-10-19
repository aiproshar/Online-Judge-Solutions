//We can traverse list rightward and add at end O(1),  but we have to insert in front as rotation
//for n-length array, if we rotate by inserting front k-elements, its equal to rotate right by (size - k) elements
//helper function to find tail pointer and list size
//read from head, extend the tail and traverse head to next
//O(n), in place rotation
//Handled Empty List by hard code
//Dont forget to mod k by list size [runtime error if we dont, size - k < 0]
//Delete front elements, preventing memory leak
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
tuple<int, ListNode*> list_helper(ListNode* head)
{
    int ans = 1;
    while(1)
    {
        if(head->next == nullptr) break;
        head = head->next;
        ans++;
    }
    return make_tuple(ans,head);
}
class Solution
{
public:
    ListNode *rotateRight(ListNode *head, int k)
    {
        if(head == nullptr) return head;
        ListNode *temp, *tail;
        int n;
        tie(n, tail) = list_helper(head);
        k = k % n;
        k = n - k;
        while(k--)
        {
            temp = new ListNode(head->val, nullptr);
            tail->next = temp;
            tail = temp;
            temp = head;
            head = head->next;
            delete temp;
        }
        return head;
    }
};
