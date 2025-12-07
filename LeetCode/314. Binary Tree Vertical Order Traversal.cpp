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

 //One of the most beautiful problems
class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {

        if(root == nullptr)return {};
        
        map<int, vector<int>>mp;

        queue<pair<TreeNode*, int>>que;

        que.emplace(root, 0);

        while(!que.empty()){

            auto lvl_size = que.size();

            while(lvl_size--){
                auto top = que.front();
                que.pop();
                mp[top.second].emplace_back(top.first->val);
                if(top.first->left != nullptr){
                    que.emplace(top.first->left, top.second - 1);
                }
                if(top.first->right != nullptr){
                    que.emplace(top.first->right, top.second + 1);
                }

            }

        }
        vector<vector<int>>ans;
        for(const auto& [key, val]: mp){
            ans.emplace_back(val);
        }

        return ans;

    }
};