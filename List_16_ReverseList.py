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

    def reverse(self, head):
        if not head or not head.next:
            return head
        cur = head
        newhead = None
        while cur:
            temp = cur.next
            cur.next = newhead
            newhead = cur
            cur = temp
        return newhead

if __name__ == '__main__':
    li = [1, 2, 3, 4, 5]
    lis = LinkList()
    for i in li:
        lis.add(i)
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node.next = node2
    node2.next = node3

    lis.show(lis.head)
    lis.show(lis.reverse(lis.head))






