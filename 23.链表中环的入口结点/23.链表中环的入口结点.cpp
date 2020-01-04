/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead)
    {
        ListNode *fast = pHead,*slow = pHead;
        while(fast!=nullptr && fast->next != nullptr){
        	slow = slow->next;
            fast = fast->next->next;
            if(fast == slow){
				fast = pHead;
                while(fast!=slow){
                    fast = fast->next;
                    slow = slow->next;
                }
            }
            if(fast==slow){
                return fast;
            }
        
        }
        return nullptr;
    }
        
};