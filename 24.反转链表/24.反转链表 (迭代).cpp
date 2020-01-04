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
    ListNode* ReverseList(ListNode* pHead) {
      if (pHead == nullptr || pHead->next == nullptr)
          return pHead;
      ListNode* pre=nullptr,*cur = pHead,*temp = nullptr;
      while(cur != nullptr){
          temp = cur->next;
          cur->next = pre;
          pre = cur;
          cur = temp;
      }
      return pre;
     }
};