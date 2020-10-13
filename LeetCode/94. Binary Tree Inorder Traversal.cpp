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

//Trivial Recursive Solution
//Common member variable, smaller call stack overhead
//Back to Back SWE explanation : https://www.youtube.com/watch?v=BHB0B1jFKQc
class Solution {
public:
    vector<int> ans;
    void traverse(TreeNode* root)
    {
        if(root->left != nullptr)
        {
            traverse(root->left);
        }
        
        ans.push_back(root->val);
        
        if(root->right != nullptr)
        {
            traverse(root->right);
        }
    }
    vector<int> inorderTraversal(TreeNode* root) {
        if(root == nullptr) return ans;
        traverse(root);
        return ans;
    }
};

//Iterative Solution
//Follow Up Question
//No call stack for easy policy management and state transfer
//Explanation : https://www.youtube.com/watch?v=nzmtCFNae9k 

class Solution {
public:
    vector<int> ans;
    
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        while(1)
        {
            if(root != nullptr)
            {
                s.push(root);
                root = root->left;
            }
            else
            {
                if(s.empty()) break;
                root = s.top();
                s.pop();
                ans.push_back(root->val);
                root = root->right;
            }
        }
        return ans;
    }
};