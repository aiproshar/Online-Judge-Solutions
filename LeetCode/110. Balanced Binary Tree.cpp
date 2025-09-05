/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
private:
    bool is_balanced;
    int depth(TreeNode* root) {
        if (root == nullptr)
            return 0;
        auto left = depth(root->left);
        auto right = depth(root->right);

        if (abs(left - right) > 1) {
            is_balanced = false;
        }

        return max(left, right) + 1;
    }

public:
    bool isBalanced(TreeNode* root) {
        is_balanced = true;
        depth(root);
        return is_balanced;
    }
};