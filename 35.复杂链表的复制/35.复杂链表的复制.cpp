/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead)
    {
        if(pHead == nullptr)
            return nullptr;
        RandomListNode* p = pHead,*temp =nullptr;
        while(p != nullptr){
            RandomListNode *q = new RandomListNode(p->label);
            temp = p->next;
            p->next = q;
            q->next = temp;
            p = temp;
        }
        p = pHead;
        while(p!=nullptr){
            if (p->random != nullptr){
                p->next->random = p->random->next;
            }
            p = p->next->next;
        }
        RandomListNode *newHead = new RandomListNode(-1);
        RandomListNode *tail = newHead;
        p = pHead;
        while(p != nullptr){
            temp = p->next->next;
            tail->next = p->next;
            p->next = temp;
            p = p->next;
            tail = tail->next;
        }
        return newHead->next;
    }
};