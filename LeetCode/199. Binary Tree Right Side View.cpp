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
//Easy traversal
//DFS, recursive method, inorder traversal (RST first)
//Root, RST, LST
//At each depth we look up do we have the right side view element in that depth ?
//If we dont have right side view element at that depth,  push to list, update current max depth
//O(n) time complexity, O(n) space complexity 
class Solution {
public:
    int explored_depth = -1;
    vector<int> rightSideView(TreeNode* root) {
        vector<int> list;
        dfs_right_to_left(root, list, 0);
        return list;
    }
    void dfs_right_to_left(TreeNode* root, vector<int>& list, int current_depth)
    {
        if(!root)
            return;
        if(current_depth > explored_depth)
        {
            explored_depth = current_depth;
            list.push_back(root->val);
        }
        dfs_right_to_left(root->right, list, current_depth + 1);
        dfs_right_to_left(root->left, list, current_depth + 1);
    }
};
