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


 //Postorder traversal
 //WHen we calculate, we try to join both lst and rst
 //if any of the subtree is negative, exclude
 //When returning to parent, we return the highest subtree. If both subtree is negative, return only the root
 //If root is subtree dont worry, the paretn process will exclude it out
class Solution {

private:
    int max_sum;

public:
    int PathSum(TreeNode* root) {

        if (root == nullptr)
            return 0;

        auto left_sum = PathSum(root->left);
        auto right_sum = PathSum(root->right);

        if (left_sum < 0)
            left_sum = 0;
        if (right_sum < 0)
            right_sum = 0;

        auto local_max = root->val + left_sum + right_sum;

        max_sum = max(max_sum, local_max);

        return root->val + max(left_sum, right_sum);
    }

    int maxPathSum(TreeNode* root) {

        max_sum = root->val;
        PathSum(root);
        return max_sum;
    }
};