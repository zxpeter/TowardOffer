class Node():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = Node()
        self.s = []

    def add(self, val):
        node = Node(val)
        if not self.root.val:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                now = queue.pop(0)
                if not now.left:
                    now.left = node
                    break
                if not now.right:
                    now.right = node
                    break
                queue.append(now.left)
                queue.append(now.right)

    def level_order_queue(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def pre_order_recursion(self, root):
        if not root:
            return 0
        nleft = self.pre_order_recursion(root.left)
        nright = self.pre_order_recursion(root.right)
        if nleft > nright:
            res = nleft + 1
        else:
            res = nright + 1
        return res


if __name__ == '__main__':
    li = [10,5,12,4,7]
    tree = Tree()
    for i in li:
        tree.add(i)
    tree.level_order_queue(tree.root)
    print('-----')
    print(tree.pre_order_recursion(tree.root))
