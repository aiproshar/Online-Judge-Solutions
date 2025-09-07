


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

 //Just traverse using the property of BST
 //When we hit a root with a null leaf, try to sit there
 //Just keep going
class Solution {

    void insert(TreeNode* root, TreeNode* node) {
        if (root->left == nullptr && node->val < root->val) {
            root->left = node;
        } else if (root->right == nullptr && node->val > root->val) {
            root->right = node;
        } else if (node->val < root->val) {
            insert(root->left, node);
        } else if (node->val > root->val) {
            insert(root->right, node);
        }
    }

public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        //Handle edge case
        if(root == nullptr){
            return new TreeNode(val);
        }
        auto node = new TreeNode(val);
        insert(root, node);
        return root;
    }
};