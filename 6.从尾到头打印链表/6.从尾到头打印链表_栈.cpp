#include <algorithm>
using namespace std;
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> ans ;
        while (head!= NULL){
            ans.push_back(head->val);
            head = head->next;
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};