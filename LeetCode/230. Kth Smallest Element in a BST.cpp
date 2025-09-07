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

 //Inorder traversal
 //When we do inorder traversal, BST gives us a sorted array
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        if(root == nullptr) return -1;
        vector<int> nums;

        auto curr = root;
        stack<TreeNode*> st;

        while(!st.empty() || curr != nullptr){

            while(curr != nullptr){
                st.emplace(curr);
                curr = curr->left;
            }
            curr = st.top();
            st.pop();
            nums.emplace_back(curr->val);
            curr = curr->right;

        }

        return nums[k-1];
    }
};