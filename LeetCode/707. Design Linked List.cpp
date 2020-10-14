//Singly linked list with head and tail pointers
//O(1) push front / push back
//O(n) add/get val at specific index
//O(n) delete at specific index
//O(1) pop_front, else O(n)
//For doubly linked list, both pop_front and pop_back will be O(1) {dequeue}
class node
{
public:
    int val;
    node* next;
    node(int val, node* next = nullptr)
        :val(val), next(next)
    {}
};
class MyLinkedList {
public:
    /** Initialize your data structure here. */
    node* head;
    node* tail;
    int size;
    MyLinkedList()
        :head(nullptr), tail(nullptr), size(0)
    {}
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index < 0 || index >= size)
            return -1;
        node* traverse = head;
        int i = 0;
        while(i < index)
        {
            i++;
            traverse = traverse->next;
        }
        return traverse->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        size++;
        if(head == nullptr)
        {
            node* temp = new node(val);
            head = temp;
            tail = temp;
        }
        else
        {
            node* temp = new node(val, head);
            head = temp;
        }
        
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        size++;
        if(tail == nullptr)
        {
            node* temp = new node(val);
            tail = temp;
            head = temp;
        }
        else
        {
            node* temp = new node(val);
            tail->next = temp;
            tail = temp;
        }
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if(index < 0 || index > size)
            return;
        if(index == 0)
        {
            addAtHead(val);
            return;
        }
        if(index == size)
        {
            addAtTail(val);
            return;
        }
        int i = 0;
        node* traverse = head;
        while(i < index - 1)
        {
            i++;
            traverse = traverse->next;
        }
        node* temp = new node(val, traverse->next);
        traverse->next = temp;
        size++;
        return;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if(index >= size)
            return;
        if(index == 0)
        {
            if(head == tail)
            {
                head = head->next;
                tail = tail->next;
            }
            else
                head = head->next;
            size--;
            return;
        }
        int i = 0;
        node* traverse = head;
        while(i + 1 < index)
        {
            i++;
            traverse = traverse->next;
        }
        //Debugged for almost four hours :(
        //For got to update tail when we remove last node
        if(traverse->next == tail)
            tail = traverse;
        traverse->next = traverse->next->next;
        size--;
        return;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */