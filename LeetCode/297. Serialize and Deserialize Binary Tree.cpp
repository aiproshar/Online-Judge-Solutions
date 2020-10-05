/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//Hard Leetcod Problem
//Recursive preorder traversal list (string) buildup
//'#' as indication of nullpointers for childrens of leaf nodes and parent with one child
//',' to separate out values
//Deserializing : Same recursive approach (bottom up)
//Pass index reference to indicate start location
//String reference for less call stack overhead
//Beats 94%
//Iterative version might be asked as follow up
//Will try to do it later :)
//Back to Back SWE explanation: https://www.youtube.com/watch?v=suj1ro8TIVY
//My implementation differs form B2B SWE, in deserialization
//Using index reference passing in much more efficient
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string datastream;
        if(!root)
            return datastream;
        preorder_stream(root, datastream);
        return datastream;
    }
    void preorder_stream(TreeNode* root, string& datastream)
    {
        if(root == nullptr)
        {
            datastream.push_back('x');
            datastream.push_back(',');
            return;
        }
        datastream += to_string(root->val);
        datastream.push_back(',');
        preorder_stream(root->left, datastream);
        preorder_stream(root->right, datastream);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(!data.size())
            return nullptr;
        int start = 0;
        return build_tree(data, start);
    }
    TreeNode* build_tree(string& data, int& start_pos)
    {
        if(data[start_pos] == 'x')
            return nullptr;
        else
        {
            string temp;
            while(data[start_pos] != ',')
            {
                temp.push_back(data[start_pos]);
                start_pos++;
            }
            TreeNode* root = new TreeNode(stoi(temp));
            start_pos++;
            root->left = build_tree(data, start_pos);
            start_pos++;
            while(data[start_pos] != ',')
                start_pos++;
            start_pos++;
            root->right = build_tree(data, start_pos);
            return root;
        }        
    }   
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));