
class inode():
    def __init__(self, data, pnext=None): # build a list, first build a node structure
        self.data = data
        self.next = pnext
    def get_data(self):
        return self.data

class ilist():
    def __init__(self, head):
        self.head = head

    def add(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!very important idea!!! thinking stack == recursive function!!
class solution():   # think of stack, then think of recursive, cause similar meaning
    def print_list(self, li, head):
        if head:
            if head.next:
                self.print_list(li, head.next)
            print(head.data)

if __name__ == '__main__':
    head = inode(1)
    node2 = inode(2)
    node3 = inode(3)
    node4= inode(4)
    li = ilist(head)
    li.add(node2)
    li.add(node3)
    li.add(node4)
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
    sol = solution()
    sol.print_list(li, head)

