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

    //This modular  functionis actually the solution of : https://leetcode.com/problems/same-tree/description/
    //It compares if two tree is identical (value and structure)
    bool compare(TreeNode* r1, TreeNode* r2){
        if(r1 == nullptr && r2 == nullptr){
            return true;
        }
        if(r1 == nullptr || r2 == nullptr){
            return false;
        }
        if(r1->val != r2->val){
            return false;
        }
        return compare(r1->left, r2->left) && 
                compare (r1->right, r2->right);
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        stack<TreeNode*> st;
        st.push(root);

        //Preorder traversal
        //Compare root first, then LST && RST
        //Only if root matches, we go forward

        while(!st.empty()){
            auto current  = st.top();
            st.pop();
            if(current == nullptr)continue;
            if(current->val == subRoot->val){
                //WhenEver our root matches, we do call compare
                //
                auto is_subtree = compare(current, subRoot);
                if(is_subtree){
                    return true;
                }
            }
            st.emplace(current->left);
            st.emplace(current->right);
        }

        return false;

    }
};