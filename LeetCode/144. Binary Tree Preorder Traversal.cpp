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
//Optimization using reference
//Not efficient to copy vector twice in each recursive call, so use reference
// Back to Back SWE explanation : https://www.youtube.com/watch?v=BHB0B1jFKQc

class Solution {
public:
    vector<int>ans;
    vector<int>& traverse(TreeNode* root, vector<int>& ans)
    {
        if(root != nullptr)
        {
            ans.push_back(root->val);
        }
        else
        {
            return ans;
        }
        if (root->left != nullptr)
        {
            preorderTraversal(root->left);
        }
        if (root->right != nullptr)
        {
            preorderTraversal(root->right);
        }
        return ans;
    }
    vector<int> preorderTraversal(TreeNode* root) {
        traverse(root, ans);
        return ans;
    }
};

//Iterative Approach
//Follow Up Question
//No call stack for easy policy management and state transfer
//Stack to mimic call stack behaviour, rst push then lst push

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