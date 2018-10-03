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

    def find_circle(self, head):
        if not head:
            return False
        p = head
        q = head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False


if __name__ == '__main__':
    lis = LinkList()
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


    # lis.show(node)
    print(lis.find_circle(node))





