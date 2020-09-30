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
//Traverse, and if we are in leaf node check if our path sum matches sum
//bottom up approach
//bottom up boolean, if we got a match(true) or not(false)
//Return logical OR of RST and LST, because we need just one match in any path
class Solution {
public:
    bool ans = false;
    bool hasPathSum(TreeNode* root, int sum) {
        if(!root)
            return false;
        return traverse(root, 0, sum);
    }
    bool traverse(TreeNode* root, int pre_sum, int sum)
    {
        if(!root->left && !root->right)
        {
            if(pre_sum + root->val == sum)
                return true;
            else
                return false;
        }
        else
        {
            bool lst = !root->left ? false : traverse(root->left, pre_sum + root->val, sum);
            bool rst = !root->right ? false : traverse(root->right, pre_sum + root->val, sum);
            return lst || rst;
        }
    }
};

//Some crackhead written 2 line solution in discussion
//Almost same as mine, he is just subtracting sum and trying to make it zero
//if somehow in any leaf sum is zero bottom up true 
class Solution {
public:
    bool hasPathSum(TreeNode *root, int sum) {
            if (root == NULL) return false;
            if (root->val == sum && root->left ==  NULL && root->right == NULL) return true;
            return hasPathSum(root->left, sum-root->val) || hasPathSum(root->right, sum-root->val);
        }
};