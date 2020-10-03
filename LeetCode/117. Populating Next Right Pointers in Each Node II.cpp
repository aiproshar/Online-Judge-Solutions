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
//Solution same as problem {116. Populating Next Right Pointers in Each Node}
//Just one line difference
//Binary tree (any type, 0, 1, 2 child)
//Compressed sparse node (skips, nullptr are not pushed in queue)
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
                if(front->left)
                    Q.push(front->left);
                if(front->right)
                    Q.push(front->right);
            }
        }
        return root;
    }
};