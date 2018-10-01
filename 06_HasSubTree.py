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
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def judge_trees(self, root1, root2):
        result = False
        if root1 and root2:
            if root1.val == root2.val:
                result = self.DoesTree1HaveTree2(root1, root2)
            if not result:
                result = self.judge_trees(root1.left, root2)
            if not result:
                result = self.judge_trees(root1.right, root2)
        return result

    def DoesTree1HaveTree2(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.DoesTree1HaveTree2(root1.left, root2.left) and \
               self.DoesTree1HaveTree2(root1.right, root2.right)




if __name__ == '__main__':
    li = [8, 8, 7, 9, 2]
    li2 = [8, 9, 2]
    tree = Tree()
    tree2 = Tree()
    for i in li:
        tree.add(i)
    for j in li2:
        tree2.add(j)
    tree.level_order_queue(tree.root)
    print('----')
    tree2.level_order_queue(tree2.root)
    print('----')

    print(tree.judge_trees(tree.root, tree2.root))


