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
//2 stack method, more complex than pre/in
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

