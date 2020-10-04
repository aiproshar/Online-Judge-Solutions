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
//Recursive Approach
//Swap siblings(not value, their address / reference)**
//recurse, if null base case
//Trivia: This problem was inspired by this original tweet by Max Howell
//https://twitter.com/mxcl/status/608682016205344768
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(!root)
            return root;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};
//Iterative solution
//As usual, very large skewed binary trees will result in call stack overflow
//So, we use our own defined stack (in heap memory) 
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        stack(TreeNode*)S;
        S.push(root);
        while(!S.empty())
        {
            auto top = S.top();
            S.pop();
            if(top)
            {
                swap(top->left, top->right);
                S.push(top->right);
                S.push(top->left);
            }
        }
        return root;
    }
};