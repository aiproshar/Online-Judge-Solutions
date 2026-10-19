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
//Basic DFS traversal
//Leaf Node - both RST and LST nullptr
//Reference passing for less call stack overhead
//O(n) runtime complexity, O(n) memory complexity
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int>  first;
        vector<int> second;
        traverse(root1, first);
        traverse(root2, second);
        if(first == second)
            return true;
        else
            return false;
        
    }
    void traverse(TreeNode* root, vector<int>& v)
    {
        if(!root)
            return;
        if(!root->left && !root->right)
        {
            v.push_back(root->val);
            return;
        }
        traverse(root->left, v);
        traverse(root->right, v);
    }
};
//Follow up question
//Iterative Approach