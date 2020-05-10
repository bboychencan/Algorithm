# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pre = ListNode(0)
        cur = pre

        while pHead1 and pHead2:
        	if pHead1.val < pHead2.val:
        		cur.next = pHead1
        		cur = cur.next
        		pHead1 = pHead1.next
        	else:
        		cur.next = pHead2
        		cur = cur.next
        		pHead2 = pHead2.next

        while pHead1:
        	cur.next = pHead1
        	cur = cur.next
        	pHead1 = pHead1.next

        while pHead2:
        	cur.next = pHead2
        	cur = cur.next
        	pHead2 = pHead2.next	

       	return pre.next