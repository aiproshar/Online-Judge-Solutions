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
//Symmetric Tree means mirrored symmetry if we draw a mirror through root
//Recursive Solution
//Call recurse with symmetric element
//First check if symmetric elements are equal or not
//If they are equal recurse call with their childs
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        return isMirror(root->left, root->right);
    }
    
    bool isMirror(TreeNode* lst, TreeNode* rst)
    {
        if(!lst || !rst)
        {
            if(!lst && !rst)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        return (lst->val == rst->val) && isMirror(lst->left, rst->right) && isMirror(lst->right, rst->left);
    }
};

//Follow Up question
//Iterative solution - no call stack
//own stack, just pop first two elements and check their symmetry
//Insert their childs in symmetric manner (first.lst--second.rst--first.rst--second.lst)
//Insert root twice initially for loop invariant
class Solution {
public:
    stack<TreeNode*> s;
    bool isSymmetric(TreeNode* root) {
        s.push(root);
        s.push(root);
        while(!s.empty())
        {
            TreeNode* t1 = s.top();
            s.pop();
            TreeNode* t2 = s.top();
            s.pop();
            if(!t1 || !t2)
            {
                if(t1 != t2)
                    return false;
                else
                    continue;
            }
            if(t1->val == t2->val)
                {
                    s.push(t1->left);
                    s.push(t2->right);
                    s.push(t1->right);
                    s.push(t2->left);
                }
                else
                    return false;
        }
        return true;
    }
};