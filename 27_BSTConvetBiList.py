class Solution:
    def Convert(self, pRootOfTree):
        self.linkedlistLast = None
        self.convertNode(pRootOfTree)
        pHead = self.linkedlistLast
        while pHead and pHead.left:
            pHead = pHead.left
        return pHead

    def convertNode(self, root):
        if not root: return
        pcurr = root
        if pcurr.left:
            self.convertNode(pcurr.left)
        pcurr.left = self.linkedlistLast
        if self.linkedlistLast:
            self.linkedlistLast.right = pcurr
        self.linkedlistLast = pcurr
        if pcurr.right:
            self.convertNode(pcurr.right)





class BinaryTreeNode():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def create_a_tree():
    node_4 = BinaryTreeNode(4)
    node_8 = BinaryTreeNode(8)
    node_6 = BinaryTreeNode(6, node_4, node_8)
    node_12 = BinaryTreeNode(12)
    node_16 = BinaryTreeNode(16)
    node_14 = BinaryTreeNode(14, node_12, node_16)
    node_10 = BinaryTreeNode(10, node_6, node_14)
    return node_10

def print_a_tree(root):
    if root is None:
        return
    print_a_tree(root.left)
    print(root.value, ' ',)
    print_a_tree(root.right)

def print_a_linked_list(head):
    print('linked_list:')
    while head is not None:
        print(head.value, ' ',)
        head = head.right
    print('')

def create_linked_list(root):
    '''构造树的双向链表，返回这个双向链表的最左结点和最右结点的指针'''
    if root is None:
        return (None, None)

    # 递归构造出左子树的双向链表
    (l_1, r_1) = create_linked_list(root.left)
    left_most = l_1 if l_1 is not None else root
    (l_2, r_2) = create_linked_list(root.right)
    right_most = r_2 if r_2 is not None else root

    # 将整理好的左右子树和root连接起来
    root.left = r_1
    if r_1 is not None:r_1.right = root
    root.right = l_2
    if l_2 is not None:l_2.left = root
    # 由于是双向链表，返回给上层最左边的结点和最右边的结点指针
    return (left_most, right_most)

if __name__ == '__main__':
    tree_1 = create_a_tree()
    print_a_tree(tree_1)
    (left_most, right_most) = create_linked_list(tree_1)
    print_a_linked_list(left_most)







class Solution:
    def Convert(self, pRootOfTree):
        self.linkedlistLast = None
        self.convertNode(pRootOfTree)
        pHead = self.linkedlistLast
        while pHead and pHead.left:
            pHead = pHead.left
        return pHead

    def convertNode(self, root):
        if not root:
            return
        pcurr = root
        if pcurr.left:
            self.convertNode(pcurr.left)
        pcurr.left = self.linkedlistLast  # the most left node.left = None
        if self.linkedlistLast:
            self.linkedlistLast.right = pcurr
        self.linkedlistLast = pcurr   # the most left node
        if pcurr.right:
            self.convertNode(pcurr.right)








