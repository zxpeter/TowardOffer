class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        self.cloneNodes(pHead)
        self.connectSiblingNodes(pHead)
        return self.reconnectNodes(pHead)

    def cloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next

    def connectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode:
            pclone = pNode.next
            if pNode.random:
                pclone.random = pNode.random.next
            pNode = pclone.next

    def reconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = None
        pCloneNode = None
        if pNode:
            pCloneHead = pCloneNode = pNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        while pNode:
            pCloneNode.next, pCloneNode = pNode.next, pCloneNode.next
            pNode.next, pNode = pCloneNode.next, pNode.next
        return pCloneHead
