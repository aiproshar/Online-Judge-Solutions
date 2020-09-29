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
class Solution {
public:
    bool ans = false;
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root)
            return false;
        return traverse(root, 0, sum);
    }
    bool traverse(TreeNode* root, int pre_sum, int sum)
    {
        if(!root->left && !root->right)
        {
            if(pre_sum + root->val == sum)
                return true;
            else
                return false;
        }
        else
        {
            bool lst = !root->left ? false : traverse(root->left, pre_sum + root->val, sum);
            bool rst = !root->right ? false : traverse(root->right, pre_sum + root->val, sum);
            return lst || rst;
        }
    }
};