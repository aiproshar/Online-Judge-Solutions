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
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {

        if (root == nullptr)
            return {};
        vector<vector<int>> traversal;
        traversal.reserve(1000);
        int lvl = 0;
        queue<TreeNode*> que;
        que.emplace(root);
        while (!que.empty()) {

            int current_lvl_size = que.size();
            traversal.push_back(vector<int>());
            while (current_lvl_size--) {
                auto front = que.front();
                que.pop();
                traversal[lvl].emplace_back(front->val);
                if(front->left != nullptr)que.emplace(front->left);
                if(front->right != nullptr)que.emplace(front->right);
            }
            lvl++;
        }

        return traversal;
    }
};