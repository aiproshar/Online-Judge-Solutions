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
//Recursive Solution
//In order traversal
//More optimization can be made by setting Flags (we got answer that its not BST, abort further recursion)
//O(n)time complexity, O(n) space complexity (skewed tree call stack size)
class Solution {
    vector<int> list;
public:
    bool isValidBST(TreeNode* root) {
        inorder(root);
        for(int i = 1; i < list.size(); i++)
        {
            if(list[i-1] < list[i])
                continue;
            else
                return false;
        }
        return true;
    }
    void inorder(TreeNode* root)
    {
        if(!root)
            return;
        inorder(root->left);
        list.push_back(root->val);
        inorder(root->right);
    }
};
//Iterative solution
//Iterative inorder traversal
//No call stack overhead
//Ref: {94. Binary Tree Inorder Traversal}
//O(n)time complexity, O(n) space complexity
class Solution {
    vector<int> list;
public:
    bool isValidBST(TreeNode* root) {
        inorder(root);
        for(int i = 1; i < list.size(); i++)
        {
            if(list[i-1] < list[i])
                continue;
            else
                return false;
        }
        return true;
    }
    void inorder(TreeNode* root)
    {
        stack<TreeNode*> S;
        while(1)
        {
            if(root != nullptr)
            {
                S.push(root);
                root = root->left;
            }
            else
            {
                if(S.empty())
                    break;
                root = S.top();
                S.pop();
                list.push_back(root->val);
                root = root->right;
            }
        }
    }
};
//Follow up
//Can you do it with constant space
//We can solve in constant space both recursively and iteratively
//Just save the last traversed value
//When we got new value, just compare
//Update last traverse value