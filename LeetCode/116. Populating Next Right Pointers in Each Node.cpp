/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
//Straight forward BFS with a Queue (iterative)
//Almost same as {102. Binary Tree Level Order Traversal} with some more constant variable
//We need to keep track of the last element of every level, because last element of a level will point to nullptr
//O(n) time complexity, O(n) space complexity
class Solution {
public:
    Node* connect(Node* root) {
        queue<Node*> Q;
        if(root)
            Q.push(root);
        while(!Q.empty())
        {
            int lvl_size = Q.size();
            for(int i = 0; i < lvl_size; i++)
            {
                auto front = Q.front();
                Q.pop();
                if(i == lvl_size - 1)
                    front->next = nullptr;
                else
                    front->next = Q.front();
                if(front->left && front->right)
                {
                    Q.push(front->left);
                    Q.push(front->right);
                }
            }
        }
        return root;
    }
};

//Follow up Question
//Can you solve it with constant space ?
//