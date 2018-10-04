
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return 
        node = head
        len = 1
        while node.next:
            node = node.next
            len += 1
        
        if k == len:
            return head
        if k > len:
            k = k % len
        node.next = head
        index = len - k - 1  
        p = head
        for i in range(0, index):
            p = p.next
        res = p.next
        p.next = None
        
        return res
