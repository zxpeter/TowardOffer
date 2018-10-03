
class Node():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = Node()

    def add(self, val):
        node = Node(val)
        if not self.root.val:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                current = queue.pop(0)
                if not current.left:
                    current.left = node
                    break
                if not current.right:
                    current.right = node
                    break
                queue.append(current.left)
                queue.append(current.right)

    def level_order_queue(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if root.left or root.right:
                root.left, root.right = root.right, root.left
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def mirror_trans(self, root):
        if not root:
            return
        print(root.val)
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        self.mirror_trans(root.left)
        self.mirror_trans(root.right)



if __name__ == '__main__':
    li = [1,2,3,4,5,6]
    tree = Tree()
    for i in li:
        tree.add(i)
    tree.level_order_queue(tree.root)
    print('-----')
    tree.mirror_trans(tree.root)
