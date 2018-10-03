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

    def merge_sorted(self, head1, head2):
        if not head1:
            return head2
        elif not head2:
            return head1
        if head1.val < head2.val:
            newhead = head1
            head1.next = self.merge_sorted(head1.next, head2)
        else:
            newhead = head2
            head2.next = self.merge_sorted(head1, head2.next)
        return newhead


if __name__ == '__main__':
    li = [1, 3, 5, 7]
    lis = LinkList()
    for i in li:
        lis.add(i)
    li2 = [2, 4, 6, 8]
    lis2 = LinkList()
    for i in li2:
        lis2.add(i)

    # lis.show(lis.head)
    lis.show(lis.merge_sorted(lis.head, lis2.head))





