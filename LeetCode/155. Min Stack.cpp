class StackNode {
public:
    StackNode(int data, StackNode* prev_node = nullptr) {
        this->data = data;
        this->upto_min =
            prev_node == nullptr ? data : min(prev_node->upto_min, data);
        this->prev_node = prev_node;
    }
    int data;
    int upto_min;
    StackNode* prev_node;
};

class MinStack {
private:
    StackNode* current;

public:
    MinStack() { current = nullptr; }

    void push(int val) {
        if (current == nullptr) {
            current = new StackNode(val);
        } else {
            auto temp = new StackNode(val, current);
            current = temp;
        }
    }

    void pop() {
        auto temp = current;
        current = current->prev_node;
        delete temp;
    }

    int top() { return current->data; }

    int getMin() {
        if (current != nullptr)
            return current->upto_min;
        return 0;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */