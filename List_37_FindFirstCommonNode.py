解题思路：


直接循环判断第一个链表的每个节点是否在第二个链表中。但，这种方法的时间复杂度为O(Length(h1) * Length(h2))。
显然，我们得找到一种更为有效的方法，至少不能是O（N^2）的复杂度。
针对第一个链表直接构造hash表，然后查询hash表，判断第二个链表的每个节点是否在hash表出现，
如果所有的第二个链表的节点都能在hash表中找到，即说明第二个链表与第一个链表有相同的节点。
时间复杂度为为线性：O(Length(h1) + Length(h2))，同时为了存储第一个链表的所有节点，空间复杂度为O(Length(h1))。
是否还有更好的方法呢，既能够以线性时间复杂度解决问题，又能减少存储空间？
转换为环的问题。把第二个链表接在第一个链表后面，如果得到的链表有环，则说明两个链表相交。
如何判断有环的问题上面已经讨论过了，但这里有更简单的方法。因为如果有环，则第二个链表的表头一定也在环上，
即第二个链表会构成一个循环链表，我们只需要遍历第二个链表，看是否会回到起始点就可以判断出来。
这个方法的时间复杂度是线性的，空间是常熟。
进一步考虑“如果两个没有环的链表相交于某一节点，那么在这个节点之后的所有节点都是两个链表共有的”这个特点，
我们可以知道，如果它们相交，则最后一个节点一定是共有的。而我们很容易能得到链表的最后一个节点，
所以这成了我们简化解法的一个主要突破口。那么，我们只要判断两个链表的尾指针是否相等。相等，则链表相交；否则，链表不相交。

所以，先遍历第一个链表，记住最后一个节点。然后遍历第二个链表，到最后一个节点时和第一个链表的最后一个节点做比较，
如果相同，则相交，否则，不相交。这样我们就得到了一个时间复杂度，它为O((Length(h1) + Length(h2))，
而且只用了一个额外的指针来存储最后一个节点。这个方法时间复杂度为线性O(N)，空间复杂度为O(1)，显然比解法三更胜一筹。

---------------------

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

