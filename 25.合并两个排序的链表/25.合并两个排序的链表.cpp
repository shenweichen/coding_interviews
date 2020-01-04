/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode* head = new ListNode(-1);
        head->next = nullptr;
        ListNode* cur = head;
        while(pHead1 != nullptr and pHead2!=nullptr){
            if (pHead1->val < pHead2->val){
                ListNode* temp = pHead1->next;
                cur->next = pHead1;
                pHead1 = temp;
            }else{
                ListNode* temp = pHead2->next;
                cur->next = pHead2;
                pHead2 = temp;
            }
            cur = cur->next;
        }
        cur->next = nullptr;
        if (pHead1 != nullptr)
            cur->next = pHead1;
        if (pHead2 != nullptr)
            cur->next = pHead2;
        return head->next;
    }
};