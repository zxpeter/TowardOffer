# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
        
        
# 翻转k-group        
def reverseKGroup(self, head, k):
    if head is None or k < 2:
        return head
    
    next_head = head
    for i in range(k - 1):
        next_head = next_head.next
        if next_head is None:
            return head
    ret = next_head
    
    current = head
    while next_head:
        tail = current
        prev = None
        for i in range(k):
            if next_head:
                next_head = next_head.next
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        tail.next = next_head or current
            
    return ret  
        
