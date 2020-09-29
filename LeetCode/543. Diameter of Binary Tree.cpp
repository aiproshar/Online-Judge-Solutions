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
//Diametr is the longest path betwen two nodes
//Bottom up approach
//DFS to find depth of lst and rst and comparing if the diameter of that three is max or not
//If max we found new global max lst + lst traverse depth, means diameter
//No separate stack for DFS, call stack DFS implementation
//Update Max Length (diameter) as we return back to root
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