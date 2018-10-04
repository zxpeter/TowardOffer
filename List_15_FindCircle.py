题目描述：输入一个单向链表，判断链表是否有环？
分析：通过两个指针，分别从链表的头节点出发，一个每次向后移动一步，另一个移动两步，
两个指针移动速度不一样，如果存在环，那么两个指针一定会在环里相遇。

问题2：若存在环，如何找到环的入口点（即上图中的结点E）？
       解答：如图中所示，设链起点到环入口点间的距离为x，环入口点到问题1中fast与low重合点的距离为y，
    又设在fast与low重合时fast已绕环n周（n>0），且此时low移动总长度为s，则fast移动总长度为2s，环的长度为r。则
        s + nr = 2s,n>0      ①
        s = x + y               ②
       由①式得  s = nr                 
       代入②式得
       nr = x + y
       x = nr - y                ③
       现让一指针p1从链表起点处开始遍历，指针p2从encounter处开始遍历，且p1和p2移动步长均为1。
    则当p1移动x步即到达环的入口点，    由③式可知，此时p2也已移动x步即nr - y步。
    由于p2是从encounter处开始移动，故p2移动nr步是移回到了encounter处，再退y步则是到了环的入口点。
    也即，当p1移动x步第一次到达环的入口点时，p2也恰好到达了该入口点。


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





