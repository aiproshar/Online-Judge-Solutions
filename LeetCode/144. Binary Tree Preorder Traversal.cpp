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

//Trivial Recursive Approach
//Not efficient to copy vector twice in each recursive call, so use member variable
//Back to Back SWE explanation : https://www.youtube.com/watch?v=BHB0B1jFKQc

class Solution {
public:
    vector<int>ans;
    void traverse(TreeNode* root)
    {
        ans.push_back(root->val);

        if(root->left != nullptr)
        {
            traverse(root->left);
        }
        
        if(root->right != nullptr)
        {
            traverse(root->right);
        }
    }
    vector<int> preorderTraversal(TreeNode* root) {
        if(root == nullptr) return ans;
        traverse(root);
        return ans;
    }
};

//Iterative Approach
//Follow Up Question
//No call stack for easy policy management and state transfer
//Stack to mimic call stack behaviour
//Go LST until nullptr
//Stack top as root (left child is nullptr)
//Go RST
//If RST nullptr, we will pop neext item from stack
class Solution {
public:
    vector<int>ans;
    vector<int> preorderTraversal(TreeNode* root)
    {
        if (root == nullptr)
            return ans;
        stack<TreeNode* >s;
        s.push(root);
        while(!s.empty())
        {
            auto top = s.top();
            s.pop();
            ans.push_back(top->val);
            if(top->right != nullptr)
            {
                s.push(top->right);
            }
            if(top->left != nullptr)
            {
                s.push(top->left);
            }
        }
        return ans;
    }
};
