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
//Diameter is the longest path betwen two nodes{from all nodes}
//Bottom up approach
//DFS to find depth of lst and rst, and comparing if the diameter of that subtree (path that goes via that root) is max or not
//If we found new max, means its diameter of current explored subtrees. Expand the subtree space to find global max
//No separate stack for DFS, call stack DFS implementation
//Update Max Length (diameter) as we return back to root (subtree search space expansion, compare with previous best and update)
class Solution {
public:
    int diameter = 0;
    int dfs_depth(TreeNode* root)
    {
        if(root == nullptr)
        {
            return 0;
        }
        int lst_depth = dfs_depth(root->left);
        int rst_depth = dfs_depth(root->right);
        //If current sub tree diameter is greater then global, update global
        diameter = lst_depth + rst_depth > diameter ? lst_depth + rst_depth : diameter;
        
        //Returning max depth of sub-tree
        return max(lst_depth,rst_depth) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        dfs_depth(root);
        return diameter;
    }
};
