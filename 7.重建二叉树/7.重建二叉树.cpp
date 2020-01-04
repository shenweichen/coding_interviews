/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
       
        if (pre.size()==0)
            return NULL;
        TreeNode* root = new TreeNode(pre[0]);
        int rootIndex = 0;
        while(vin[rootIndex]!=root->val)
            rootIndex++;
        int leftNum = rootIndex;
        int rightNum = pre.size()-leftNum-1;
        root->left = reConstructBinaryTree(vector<int>(pre.begin()+1,pre.begin()+1+leftNum),vector<int>(vin.begin(),vin.begin()+leftNum));
        root->right = reConstructBinaryTree(vector<int>(pre.begin()+1+leftNum,pre.end()),vector<int>(vin.begin()+leftNum+1,vin.end())); 
        return root;
        
    }
};