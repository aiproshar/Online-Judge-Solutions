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
//Straight-forward recursive solution
//To rebuild tree we need two data : root and elemets in LST ans RST
//From postorder/preorder we can find root->val (last/first list element)
//After finding root->val, we can split the inorder list into two parts ( [...] root->val [...] )
//Split postorder list to LST / RST based on size of splitted inorder list 
//In summary, 
//1. Find root->val from postorder (last element)
//2. Find root->val in inorder (linear scan root->val compare), all the elements in left of root->val belongs to LST and on right belongs to RST
//3. Split the inorder into two list, start.....before_root->val(LST) and after_root->val.....end(RST)
//4. On postorder root is the last element, so ignore last element and split postorder based on the split size of inorder list (size of LST or RST elemets always same whatever traversal list it is)
//5. Recurse on LST and RST
//Check if list is empty(no element on that subtree), return nullptr
//Solution is not optimal(theory ok, bad implementation), because vector copy overhead. (bad runtime + excessive memory usage)
//Jenny mams explanation: https://www.youtube.com/watch?v=s5XRtcud35E
//More optimal Solution: Better if we define our own function and just pass the start, end location of vectors in call stack(slicing behaviour like NumPy)
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if(!inorder.size())
            return nullptr;
        TreeNode* root = new TreeNode;
        root->val = postorder[postorder.size() - 1];
        vector<int> lst_inorder, rst_inorder, lst_postorder, rst_postorder;
        auto it_inorder = inorder.begin();
        auto it_postorder = postorder.begin();
        for(; *it_inorder != root->val; it_inorder++, it_postorder++)
        {
            lst_inorder.push_back(*it_inorder);
            lst_postorder.push_back(*it_postorder);
        }
        it_inorder++;
        for(; it_inorder != inorder.end(); it_inorder++, it_postorder++)
        {
            rst_inorder.push_back(*it_inorder);
            rst_postorder.push_back(*it_postorder);
        }
        root->left = buildTree(lst_inorder, lst_postorder);
        root->right = buildTree(rst_inorder, rst_postorder);
        return root;
    }
};

//Optimized Solution
//No call stack vector copy overhead
//Just keep track of index
//Class memeber inorder and postorder list copy, so accesable from any call stack
//We need size information for end offset (start + sz - 1) //first forloop in first solution
//First solution : 240ms/162 MB, optimized solution: 28 ms, 27 MB (10x improvement)
//Similarity with NumPy slice, we dont copy or split or modity actual list
//We just select sublist by passing index values (no copy overhead)
class Solution {
    vector<int> inorder;
    vector<int> postorder;
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        Solution::inorder = inorder;
        Solution::postorder = postorder;
        return optimized_buildTree(0, inorder.size() - 1, 0, postorder.size() - 1);
    }
    TreeNode* optimized_buildTree(int inorder_start, int inorder_end, int post_start, int post_end)
    {
        if(inorder_end < inorder_start || post_end < post_start)
            return nullptr;
        TreeNode* root = new TreeNode(postorder[post_end]);
        int lst_inorder_start , lst_inorder_end, rst_inorder_start, rst_inorder_end, lst_post_start, lst_post_end, rst_post_start, rst_post_end;
        
        int root_idx;
        int sz = 0;
        for(root_idx = inorder_start; inorder[root_idx] != root->val; root_idx++)
            sz++;
        lst_inorder_start = inorder_start;
        lst_inorder_end = root_idx - 1;
        lst_post_start = post_start;
        lst_post_end = post_start + sz - 1;
        
        rst_inorder_start = root_idx + 1;
        rst_inorder_end = inorder_end;
        rst_post_start = lst_post_end + 1;
        rst_post_end = post_end - 1;
        root->left = optimized_buildTree(lst_inorder_start, lst_inorder_end, lst_post_start, lst_post_end);
        root->right = optimized_buildTree(rst_inorder_start, rst_inorder_end, rst_post_start, rst_post_end);
        return root;

    }
};
