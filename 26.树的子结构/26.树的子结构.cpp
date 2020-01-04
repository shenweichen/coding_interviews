/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if (pRoot1 == nullptr || pRoot2 == nullptr)
            return false;
        
        bool ans = false;
        preOrder(pRoot1,pRoot2,ans);
        return ans;
        
    }
    bool judge(TreeNode* A,TreeNode* B){
        if (A!=nullptr&&B!=nullptr){
            if (A->val!=B->val)
                return false;
            else
                return judge(A->left,B->left)&&judge(A->right,B->right);
        }else
            return (B==nullptr);
    }
    void preOrder(TreeNode* A,TreeNode*B,bool& ans){
        if(A==nullptr||ans)
            return ;
        ans = judge(A,B);
        preOrder(A->left,B,ans);
        preOrder(A->right,B,ans);
    }
};