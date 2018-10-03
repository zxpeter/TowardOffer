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

    def pre_order_recursion(self, root, sum):
        if not root:
            return
        # print(root.val)
        self.s.append(root)
        sum += root.val
        if root.left or root.right:
            self.pre_order_recursion(root.left, sum)
            self.pre_order_recursion(root.right, sum)
        else:
            if sum == 22:
                # print(root.val)
                for i in self.s:
                    print(i.val)
                print('---')
            sum -= root.val
            self.s.pop()

if __name__ == '__main__':
    li = [10,5,12,4,7]
    tree = Tree()
    for i in li:
        tree.add(i)
    tree.level_order_queue(tree.root)
    print('-----')
    sum = 0
    tree.pre_order_recursion(tree.root, sum)
