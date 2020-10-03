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
//The Solution is intuitive using constant space, kinda hard to describe without images but lets give it a try
//           O
//          / \
//         /   \
//        O-->--O-->x //upper level (parent and uncle)
//       / \   / \
//      /   \ /   \
//     O-->-O O-->-O  //current level (siblings and cousins)
//its easy to create link between siblings, but for cousins we should go to upper layer
//we dont need to traverse back all the way to root, because we can find the uncle from the next pointer from parent
//So, right child next pointer to cousin, find cousin through parent next (parent->next is uncle)
//next pointer default constructor sets to nullptr, required by our algorithm
class Solution {
public:
    Node* connect(Node* root) {
        if(!root)
            return nullptr;
        Node* level = root;
        while(level->left)
        {
            Node* parent = level;
            while(parent)
            {
                parent->left->next = parent->right;               //siblings relation
                if(parent->next)                                  //check if we have uncle or not
                    parent->right->next = parent->next->left;     //cousins relation, relation found through uncle(uncle == parent->next);
                parent = parent->next;                            //current parent is done(all relation of his childs established), loop invariant to uncle
            }
            level = level->left;                                  //Next level, starting from left most node (childs are parent)
        }
        return root;     
    }
};