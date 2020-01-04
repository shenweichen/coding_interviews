/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool isSymmetrical(TreeNode* pRoot)
    {
    	if(pRoot == nullptr)
            return true;
        return isSym(pRoot->left,pRoot->right);
    }
    bool isSym(TreeNode* left,TreeNode* right){
        if(left==nullptr&&right==nullptr)
            return true;
        if(left==nullptr||right==nullptr)
            return false;
        return (left->val==right->val)&&isSym(left->right,right->left)&&isSym(left->left,right->right);
    }

};