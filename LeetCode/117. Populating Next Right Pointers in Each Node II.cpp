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
//O(n) memory (just like unoptimized 116 solution)
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
//Follow up
//Constant space method
// Similar to {116. Populating Next Right Pointers in Each Node} with modification
//First loop to iterate levels
//Second loop to nodes of a specific level
//First we need to find the very first leftmost pointer for next iteration
//next_lvl_start pointer to find the leftmost(first) element of childs of current level
//On every level we use a current pointer to iterate the parents of that level, temp pointer to iterate childs
//When we find a new child, we make temp->next that child and update temp to newly founded child
//when current is null means all nodes of that level visited, their childs relation established with siblings and cousins.
//So we break loop go to next level, (using current = next_lvl_start)
//if current is null in the begining(means, next_lvl_start == null) no childs exist in lower depths, terminate outer loop
//8 ms runtime, beats 99.9%
class Solution {
public:
    Node* connect(Node* root) {
        Node* current = root;
        while(current)
        {
            Node* next_lvl_start = nullptr;
            Node* temp = nullptr;
            while(current)
            {
                if(current->left)
                {
                    if(!next_lvl_start)
                    {
                        next_lvl_start = current->left;
                        temp = current->left;
                    }
                    else
                    {
                        temp->next = current->left;
                        temp = temp->next;
                    }
                }
                if(current->right)
                {
                    if(!next_lvl_start)
                    {
                        next_lvl_start = current->right;
                        temp = current->right;
                    }
                    else
                    {
                        temp->next = current->right;
                        temp = temp->next;
                    }
                }
                current = current->next;
            }
            current = next_lvl_start;
        }
        return root;
    }
};