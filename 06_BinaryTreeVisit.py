
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = Node()

    def build(self, data):
        node = Node(data)
        if not self.root.data: # value! because it do have an object
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                first_node = queue.pop(0)
                if not first_node.left:
                    first_node.left = node
                    return
                elif not first_node.right:
                    first_node.right = node
                    return
                else:
                    queue.append(first_node.left)
                    queue.append(first_node.right)

    def level_order_queue(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            current_node = queue.pop(0)
            print(current_node.data)
            if current_node.left:
               queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def pre_order_recursion(self, root):
        if not root:
            return
        print(root.data)
        self.pre_order_recursion(root.left)
        self.pre_order_recursion(root.right)

    def in_order_recursion(self, root):
        if not root:
            return
        self.in_order_recursion(root.left)
        print(root.data)
        self.in_order_recursion(root.right)

    def post_order_recursion(self, root):
        if not root:
            return
        self.post_order_recursion(root.left)
        self.post_order_recursion(root.right)
        print(root.data)

    def pre_order_stack(self, root):
        if not root:
            return
        mystack = []
        node = root
        while mystack or node:
            while node:
                print(node.data)
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            node = node.right

    def in_order_stack(self, root):
        if not root:
            return
        mystack = []
        node = root
        while mystack or node:
            while node:
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            print(node.data)
            node = node.right

    def post_order_stack(self, root):
        if not root:
            return
        mystack1 = []
        mystack2 = []
        node = root
        while mystack1 or node:
            while node:
                mystack1.append(node)
                mystack2.append(node)
                node = node.right
            node = mystack1.pop()
            node = node.left
        while mystack2:
            print(mystack2.pop().data)




if __name__ == '__main__':
    li = [1,2,3,4,5,6]
    tree = Tree()
    for i in li:
        tree.build(i)
    # tree.level_order_queue(tree.root)
    tree.pre_order_recursion(tree.root)
    print('-----')
    tree.pre_order_stack(tree.root)
    print('-----')
    tree.in_order_recursion(tree.root)
    print('-----')
    tree.in_order_stack(tree.root)
    print('-----')
    tree.post_order_recursion(tree.root)
    print('-----')
    tree.post_order_stack(tree.root)


