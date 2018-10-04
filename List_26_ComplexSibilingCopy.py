def copyRandomList(self, head):
    if not head:
        return None
    p = head
    while p:
        node = RandomListNode(p.label)
        node.next = p.next
        p.next = node
        p = p.next.next
        # p = node.next
    p = head    
    while p:
        if p.random:
            p.next.random = p.random.next
        p = p.next.next
    newhead = head.next
    pold = head
    pnew = newhead
    while pnew.next:
        pold.next = pnew.next
        pold = pold.next
        pnew.next = pold.next
        pnew = pnew.next
    pold.next = None
    pnew.next = None
    return newhead
