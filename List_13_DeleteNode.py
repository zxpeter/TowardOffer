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

    def delete_node(self, head, val):
        if not head:
            return
        if head.val == val:
            return head.next
        prev = head
        curr = prev.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return head

    def delete_node_linear(self, head, node):
        if not head:
            return
        if not head.next:   # only one node in list
            head.val = None
        elif not node.next:
            curr = head
            while curr.next != node:
                curr.next = curr
            curr.next = None
        else:
            node.val = node.next.val
            node.next = node.next.next

if __name__ == '__main__':
    li = [1, 2, 3, 4]
    lis = LinkList()
    for i in li:
        lis.add(i)
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node.next = node2
    node2.next = node3

    lis.show(node)
    # lis.delete_node(lis.head, 3)
    lis.delete_node_linear(node, node)
    lis.show(node)
    # lis.reverse_show(lis.head)










