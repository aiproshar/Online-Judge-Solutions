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
//Optimized Solution - 4ms
//My First Solution was stupid, took 60 ms and 23 MB
//BFS but modified
//We only need level data, not parent
//Explore all modes of same level in one go, use size of queue to trace elements of same level
//Repeat and explore next levels until queue is empty
//Optimized solution from sample submission
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        vector<vector<int> > ans;
        queue<TreeNode*> Q;
        
        if(root != nullptr)
        {
            Q.push(root);
        }
        while(!Q.empty())
        {
            int current_level_size = Q.size();
            vector<int>current_level;
            while(current_level_size--)
            {
                auto node = Q.front();
                current_level.push_back(node->val);
                Q.pop();
                if(node->left != nullptr)
                {
                    Q.push(node->left);
                }
                if(node->right != nullptr)
                {
                    Q.push(node->right);
                }
            }
            ans.push_back(current_level);
        }
        return ans;
    }
};