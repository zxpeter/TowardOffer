class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkList():
    def __init__(self):
        self.head = Node()

    def add(self, val):
        node = Node(val)
        if not self.head.val:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def show(self, node):
        while node:
            print(node.val)
            node = node.next

    def find_mid(self, head):
        if not head:
            return False
        p = head
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next
        return p.val

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    # li = [1, 2, 3, 4, 5]
    li = [1, 2, 3, 4, 5, 6]
    lis = LinkList()
    for i in li:
        lis.add(i)

    lis.show(lis.head)
    print(lis.find_mid(lis.head))


