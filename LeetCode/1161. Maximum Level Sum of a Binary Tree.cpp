

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

 //Level oreder traversal AKA BFS
 //Calculate total_sum of each level
 //Compare with global max sum
 //store depth of max sum
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int max_lvl = 1;
        int max_sum = root->val;

        queue<TreeNode*> que;
        que.emplace(root);    
        int current_lvl = 1; 

        while (!que.empty()) {
            auto current_sum = 0;
            auto current_lvl_size = que.size(); 
            while (current_lvl_size--) {
                auto current_node = que.front();
                que.pop();
                current_sum += current_node->val;
                // push non-null childs
                if (current_node->left != nullptr) {
                    que.emplace(current_node->left);
                }
                if (current_node->right != nullptr) {
                    que.emplace(current_node->right);
                }
            }
            if (current_sum > max_sum) {
                max_sum = current_sum;
                max_lvl = current_lvl;
            }
            current_lvl++;
        }
        return max_lvl;
    }
};