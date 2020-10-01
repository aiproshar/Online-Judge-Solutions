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
//Almost same as post order + inorder
//Optimized solution
//Explanation and implementation details Ref: 106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution {
public:
    vector<int> inorder;
    vector<int> preorder;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        Solution::inorder = inorder;
        Solution::preorder = preorder;
        return optimized_buildTree(0, inorder.size() - 1, 0, preorder.size() - 1);
    }
    TreeNode* optimized_buildTree(int inorder_start, int inorder_end, int pre_start, int pre_end)
    {
        if(inorder_end < inorder_start || pre_end < pre_start)
            return nullptr;
        TreeNode* root = new TreeNode(preorder[pre_start]);
        int lst_inorder_start , lst_inorder_end, rst_inorder_start, rst_inorder_end, lst_pre_start, lst_pre_end, rst_pre_start, rst_pre_end;
        
        int root_idx;
        int sz = 0;
        for(root_idx = inorder_start; inorder[root_idx] != root->val; root_idx++)
            sz++;
        lst_inorder_start = inorder_start;
        lst_inorder_end = root_idx - 1;
        lst_pre_start = pre_start + 1;
        lst_pre_end = pre_start + sz;
        
        rst_inorder_start = root_idx + 1;
        rst_inorder_end = inorder_end;
        rst_pre_start = lst_pre_end + 1;
        rst_pre_end = pre_end;
        root->left = optimized_buildTree(lst_inorder_start, lst_inorder_end, lst_pre_start, lst_pre_end);
        root->right = optimized_buildTree(rst_inorder_start, rst_inorder_end, rst_pre_start, rst_pre_end);
        return root;

    }
};