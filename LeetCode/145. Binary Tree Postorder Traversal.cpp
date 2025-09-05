/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

//Trivial Recursive
//Reference and Explanation : 94 and 144

class Solution {
public:
    vector<int> ans;
    void traverse(TreeNode* root)
    {
        if(root->left != nullptr)
        {
            traverse(root->left);
        }
        if(root->right != nullptr)
        {
            traverse(root->right);
        }
        ans.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        if(root == nullptr) return ans;
        traverse(root);
        return ans;
        
    }
};

//Iterative Solution
//2 stack method, more complex than pre-order/in-order
//Intermediate stack and Ans stack
//Explanation : https://www.youtube.com/watch?v=qT65HltK2uE 
//There is some one stack bullshit hard implementation, not interested :P 

class Solution {
public:
    vector<int> ans;
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> s1;
        stack<TreeNode*> s2;
        if(root == nullptr) return ans;
        s1.push(root);
        while(!s1.empty())
        {
            root = s1.top();
            s1.pop();
            s2.push(root);
            if(root->left != nullptr)
            {
                s1.push(root->left);
            }
            if(root->right != nullptr)
            {
                s1.push(root->right);
            }
        }
        while(!s2.empty())
        {
            auto temp = s2.top();
            s2.pop();
            ans.push_back(temp->val);
        }
        return ans;
    }
};

//Iterative Solution - After 5 years i came up with this on my own while trying
//Life's fked up, for good !
//In post order traversal we need to visit left and right first, then root
//How we keep track that, HashMApUh! So, key is node pointer, value is boolean
// Everytime we check the top node from stack, we check if its left child and right are visited or not
//If not we push them into the stack, push right first and then left (LIFO, left come first)
//If we visited both subtree, pop that from the stack, mark it visited on the hashTable and
//Also insert that on traverse vector YaY!
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        unordered_map<TreeNode*, bool> mp;
        mp.reserve(200);
        //We will push all the subtree without null check
        //So when nullpointers in the stack, they are visited
        mp[nullptr] = true;
        vector<int> traversal;

        st.emplace(root);
        while (!st.empty()) {
            auto top = st.top();

            //Some nullpointer, lea edges decendent
            if (top == nullptr) {
                st.pop();
                continue;
            }
            //Some node, of which both LST and RST are marked as visited
            //The node itself could be a leaf node, means both left and right is nullptr
            //We dont care, cause we already handled nullpointers present in the stack
            if (mp.contains(top->left) && mp.contains(top->right)) {
                traversal.emplace_back(top->val);
                mp[top] = true;
                st.pop();
            } else {

                //Childs are not visited, we dont check the condition of each child separately
                //cause we push them both at the same time, even one is null or both is null
                //Handling the null in the stack made this hell easier
                st.emplace(top->right);
                st.emplace(top->left);
            }
        }
        return traversal;
    }
};