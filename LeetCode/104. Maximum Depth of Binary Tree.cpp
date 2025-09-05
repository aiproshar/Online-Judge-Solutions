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
//Bottom up approach
//Return value as state management
//LeetCode card : https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/534/
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root)
        {
            return 0;
        }
        int left_depth = maxDepth(root->left);
        int right_depth = maxDepth(root->right);
        return max(left_depth, right_depth) + 1;   
    }
};

//iterative solution
//BFS
//We keep count on how many levels we explored
//Before exploring the current level, we save its size so we dont explore its child
// Each exploration, depth++
//time O(n) , space O(n)
class Solution{
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr)return 0;
        queue<TreeNode*> que;
        que.push(root);

        int depth = 0;
        while(!que.empty()){
            auto queue_size = que.size();
            while(queue_size--){
                auto curr = que.front();
                que.pop();
                if(curr->left != nullptr)que.push(curr->left);
                if(curr->right != nullptr)que.push(curr->right);
            }
            depth++;
        }
        
        return depth;
        
    }
};