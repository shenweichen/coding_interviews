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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
      ListNode* fast = pListHead;
      ListNode* slow = pListHead;
      while(fast != nullptr && k!=0){
          fast = fast->next;
          k--;
      };
      if (k>0)
          return nullptr;
      while(fast != nullptr){
          fast = fast->next;
          slow = slow->next;
      };
      return slow;
    }
};