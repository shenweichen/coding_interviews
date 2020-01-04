# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        dummy = ListNode(0)
        dummy.next = pHead
        prev = dummy
        cur = pHead
        while(cur is not None):
            if cur.next is not None and cur.next.val == cur.val:
                val = cur.val
                while(cur is not None and cur.val==val):
                    del_node = cur
                    prev.next = cur.next
                    cur = cur.next
                    del del_node
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next