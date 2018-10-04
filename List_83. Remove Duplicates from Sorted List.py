class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: 
            return
        node = head
        while node:
            prev = node
            while node and node.val == prev.val:
                node = node.next
            prev.next = node
        return head
        
        
        
class Solution(object):
    def deleteDuplicates2(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
