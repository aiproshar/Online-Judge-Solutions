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
//From postorder/preorder we can find root
//After finding root from inorder we can find the elements of RST and LST, by spliting the scanning root value (no duplicates precondition)
//Split postorder based on size of splitted list
//In summary, 
//1. Find root from postorder (last element)
//2. Find root in inorder (linear scan root-> val compare), all the elements in left of root belongs to LST and on right belongs to RST (inorder : LST-ROOT-RST)
//3. Split the inorder into two list, start.....before_root(LST) and after_root.....end(RST)
//4. On postorder root is the last element, so ignore last element and split postorder based on the split size of inorder list (size of LST or RST elemets always same whatever traversal list it is)
//5. Recurse on LST and RST
//Check if list is empty(no element on that subtree), return nullptr
//Solution is not optimal, because vector copy overhead. (bad runtime + excessive memory usage)
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
