/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
        
    }
};
*/
class Solution {
public:
    TreeLinkNode* GetNext(TreeLinkNode* pNode)
    {
        if (pNode->right != nullptr){
            TreeLinkNode *p = pNode->right;
            while(p->left != nullptr){
                p = p->left;
			}
            return p;
        }
        while(pNode->next!=nullptr){
            if(isLeftChild(pNode))
                return pNode->next;
            pNode = pNode->next;
        }
        return nullptr;
    }
    bool isLeftChild(TreeLinkNode* p){
        if(p->next!=nullptr && p->next->left == p)
            return true;
        else
		return false;
    }
};