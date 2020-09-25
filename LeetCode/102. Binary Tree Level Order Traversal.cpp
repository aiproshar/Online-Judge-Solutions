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
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        unordered_map<TreeNode*, int>  level;
        unordered_map<TreeNode*, TreeNode*>  parent;
        vector<vector<int> > ans(10000,vector<int>{});
        queue<TreeNode*> Q;
        if(root != nullptr)
        {
            Q.push(root);
            level[root] = 0;
            ans[level[root]].push_back(root->val);
        }
        while(!Q.empty())
        {
            auto node = Q.front();
            Q.pop();
            if(node->left != nullptr)
            {
                Q.push(node->left);
                parent[node->left] = node;
                level[node->left] = level[node] + 1;
                ans[level[node->left]].push_back(node->left->val);
            }
            if(node->right != nullptr)
            {
                Q.push(node->right);
                parent[node->right] = node;
                level[node->right] = level[node] + 1;
                ans[level[node->right]].push_back(node->right->val);
            }
        }
        while(ans.size() > 0)
        {
            if(ans[ans.size() - 1] == vector<int>{})
                ans.pop_back();
            else
                break;
        }
        return ans;
    }
};