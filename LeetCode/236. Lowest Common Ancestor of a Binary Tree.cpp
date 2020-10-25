/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//recursive approach
//2 Cases,case 1: our current node has one value, and another in in either LST or RST
//        case 2: We have one in LST and another in RST
//termination flag for runtime optimization (if we already have ans, why recurse any more!)
//If both values are in either LST or RST, its not an ancestor
class Solution {
public:
    TreeNode* ans;
    bool terminate = false;
    bool found(TreeNode* root, TreeNode* p, TreeNode* q)
    {
        if(!root || terminate)
            return 0;
        bool lst_found = found(root->left, p, q);
        bool rst_found = found(root->right,p, q);
        if(root->val == p->val || root->val == q->val)
        {
            if(lst_found || rst_found)
            {
                ans = root;
                terminate = true;
                return false;
            }
            else
                return true;
        }
        else if(lst_found && rst_found)
        {
            ans = root;
            terminate = true;
            return false;
        }
        return lst_found || rst_found;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        found(root, p,q);
        return ans;
    }
};
