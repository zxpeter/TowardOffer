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

    def find_remaining(self, head, m):
        if not head:
            return
        curr = head
        if curr == curr.next:
            return curr
        for i in range(0, m-1):
            curr = curr.next
        print(curr.val)
        curr.val = curr.next.val
        curr.next = curr.next.next
        return self.find_remaining(curr, m)

if __name__ == '__main__':
    lis = LinkList()
    node5 = Node(0)
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node5.next = node
    node.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5


    print(lis.find_remaining(node5, 3).val)




