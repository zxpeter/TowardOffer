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
# 方法一：栈，逆序输入，最后弹出，末尾节点都是相同的
# 方法二：指针

    def find_common(self, head1, head2):
        if not head1 or not head2:
            return
        curr1 = head1
        curr2 = head2
        len1, len2 = 0, 0
        while curr1:
            curr1 = curr1.next
            len1 += 1
        while curr2:
            curr2 = curr2.next
            len2 += 1
        print(len1, len2)
        curr1 = head1
        curr2 = head2
        if len1 > len2:
            for i in range(0, (len1 - len2)):
                curr1 = curr1.next
        else:
            for i in range(0, (len2 - len1)):
                curr2 = curr2.next

        print(curr1.val, curr2.val)

        while curr1:
            if curr1 == curr2:
                print(curr1.val)
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next

if __name__ == '__main__':
    lis = LinkList()
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node.next = node2
    node2.next = node3
    node3.next = node4

    # node_ = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)

    # node_.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    node5 = Node(5)
    node6 = Node(6)
    node4.next = node5
    node_4.next = node5
    node5.next = node6

    lis.find_common(node, node_2)

