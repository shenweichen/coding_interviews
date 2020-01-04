/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> ans;
    vector<int> printListFromTailToHead(ListNode* head) {
        printNext(head);
        return ans;
    }
    void printNext(ListNode* head){
        if (head != nullptr)
        {
        	printNext(head->next);
            ans.push_back(head->val);
        }
    }
};