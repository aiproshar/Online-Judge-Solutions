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
//Reference and Explanation : 94 and 144