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

    def reverse_show(self, node):
        if not node:
            return
        self.reverse_show(node.next)
        print(node.val)


if __name__ == '__main__':
    li = [1,2,3,4]
    lis = LinkList()
    for i in li:
        lis.add(i)
    # lis.show(lis.head)
    lis.reverse_show(lis.head)

